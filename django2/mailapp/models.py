from django.db import models


class EmailMessage(models.Model):
    class Folder(models.TextChoices):
        INBOX = "inbox", "Inbox"
        SENT = "sent", "Sent"
        ARCHIVE = "archive", "Archive"
        TRASH = "trash", "Trash"

    sender = models.EmailField()
    recipient = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    folder = models.CharField(max_length=20, choices=Folder.choices, default=Folder.INBOX)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.subject} ({self.sender} -> {self.recipient})"
