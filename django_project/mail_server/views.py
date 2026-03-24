import json

from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_GET, require_http_methods, require_POST

from .models import EmailMessage


def _parse_json(request: HttpRequest) -> dict:
    try:
        return json.loads(request.body.decode("utf-8") or "{}")
    except (json.JSONDecodeError, UnicodeDecodeError):
        return {}


def _serialize_email(message: EmailMessage) -> dict:
    return {
        "id": message.id,
        "sender": message.sender,
        "recipient": message.recipient,
        "subject": message.subject,
        "body": message.body,
        "is_read": message.is_read,
        "folder": message.folder,
        "created_at": message.created_at.isoformat(),
        "updated_at": message.updated_at.isoformat(),
    }


@require_POST
def send_email(request: HttpRequest) -> JsonResponse:
    data = _parse_json(request)
    sender = data.get("sender")
    recipient = data.get("recipient")
    subject = data.get("subject", "")
    body = data.get("body", "")

    if not sender or not recipient:
        return JsonResponse(
            {"error": "Fields 'sender' and 'recipient' are required."},
            status=400,
        )

    message = EmailMessage.objects.create(
        sender=sender,
        recipient=recipient,
        subject=subject,
        body=body,
        folder=EmailMessage.Folder.INBOX,
    )
    return JsonResponse({"message": _serialize_email(message)}, status=201)


@require_GET
def api_root(_: HttpRequest) -> JsonResponse:
    base = "/main/django_project/mail_server"
    return JsonResponse(
        {
            "service": "mail_server-api",
            "endpoints": {
                "send_email": f"POST {base}/emails/send/",
                "list_emails": f"GET {base}/emails/?user_email=<email>&box=inbox|sent|archive|trash",
                "get_email": f"GET {base}/emails/<id>/?user_email=<email>",
                "move_email": f"PATCH {base}/emails/<id>/move/",
                "delete_email": f"DELETE {base}/emails/<id>/delete/?user_email=<email>",
            },
        }
    )


@require_GET
def list_emails(request: HttpRequest) -> JsonResponse:
    user_email = request.GET.get("user_email")
    box = request.GET.get("box", EmailMessage.Folder.INBOX)

    if not user_email:
        return JsonResponse({"error": "Query param 'user_email' is required."}, status=400)

    if box == EmailMessage.Folder.SENT:
        queryset = EmailMessage.objects.filter(sender=user_email)
    else:
        queryset = EmailMessage.objects.filter(recipient=user_email, folder=box)

    emails = [_serialize_email(message) for message in queryset]
    return JsonResponse({"results": emails})


@require_GET
def get_email(request: HttpRequest, message_id: int) -> JsonResponse:
    user_email = request.GET.get("user_email")
    if not user_email:
        return JsonResponse({"error": "Query param 'user_email' is required."}, status=400)

    try:
        message = EmailMessage.objects.get(id=message_id)
    except EmailMessage.DoesNotExist:
        return JsonResponse({"error": "Message not found."}, status=404)

    if user_email not in {message.sender, message.recipient}:
        return JsonResponse({"error": "Access denied."}, status=403)

    if user_email == message.recipient and not message.is_read:
        message.is_read = True
        message.save(update_fields=["is_read", "updated_at"])

    return JsonResponse({"message": _serialize_email(message)})


@require_http_methods(["PATCH"])
def move_email(request: HttpRequest, message_id: int) -> JsonResponse:
    data = _parse_json(request)
    user_email = data.get("user_email")
    target_folder = data.get("folder")

    if not user_email or not target_folder:
        return JsonResponse(
            {"error": "Fields 'user_email' and 'folder' are required."},
            status=400,
        )

    valid_folders = {choice for choice, _ in EmailMessage.Folder.choices}
    if target_folder not in valid_folders:
        return JsonResponse(
            {"error": f"Folder must be one of: {', '.join(sorted(valid_folders))}."},
            status=400,
        )

    try:
        message = EmailMessage.objects.get(id=message_id)
    except EmailMessage.DoesNotExist:
        return JsonResponse({"error": "Message not found."}, status=404)

    if user_email != message.recipient:
        return JsonResponse({"error": "Only recipient can move this message."}, status=403)

    message.folder = target_folder
    message.save(update_fields=["folder", "updated_at"])
    return JsonResponse({"message": _serialize_email(message)})


@require_http_methods(["DELETE"])
def delete_email(request: HttpRequest, message_id: int) -> JsonResponse:
    user_email = request.GET.get("user_email")
    if not user_email:
        return JsonResponse({"error": "Query param 'user_email' is required."}, status=400)

    try:
        message = EmailMessage.objects.get(id=message_id)
    except EmailMessage.DoesNotExist:
        return JsonResponse({"error": "Message not found."}, status=404)

    if user_email not in {message.sender, message.recipient}:
        return JsonResponse({"error": "Access denied."}, status=403)

    message.delete()
    return JsonResponse({}, status=204)
