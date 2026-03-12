from django.db import models

class Folder(models.Model):
    '''
    Модель представляющая папку почтового ящика
    '''
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class EmailMessage(models.Model):
    '''
    Модель электронного письма
    '''
    sender = models.CharField(max_length=255)
    recipient = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='messages')
    is_deleted_permanently = models.BooleanField(default=False)

    class Meta:
        '''
        Мета-класс для настройки модели
        '''
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.subject} ({self.folder.name})"
