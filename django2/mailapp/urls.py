from django.urls import path

from . import views

urlpatterns = [
    path("", views.api_root, name="api_root"),
    path("emails/send/", views.send_email, name="send_email"),
    path("emails/", views.list_emails, name="list_emails"),
    path("emails/<int:message_id>/", views.get_email, name="get_email"),
    path("emails/<int:message_id>/move/", views.move_email, name="move_email"),
    path("emails/<int:message_id>/delete/", views.delete_email, name="delete_email"),
]
