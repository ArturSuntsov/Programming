from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import EmailMessage, Folder
from .serializers import EmailMessageSerializer, FolderSerializer

class EmailMessageViewSet(viewsets.ModelViewSet):
    '''
    Контроллер для управления письмами
    '''
    queryset = EmailMessage.objects.filter(is_deleted_permanently=False)
    serializer_class = EmailMessageSerializer

    def get_queryset(self):
        '''
        Метод фильтрации писем по папке
        '''
        queryset = super().get_queryset()
        folder_slug = self.request.query_params.get('folder')
        if folder_slug:
            queryset = queryset.filter(folder__slug=folder_slug)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        '''
        Метод просмотра письма с отметкой о прочтении
        '''
        instance = self.get_object()
        if not instance.is_read:
            instance.is_read = True
            instance.save(update_fields=['is_read'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def move(self, request, pk=None):
        '''
        Метод перемещения письма между папками
        '''
        message = self.get_object()
        folder_slug = request.data.get('folder_slug')
        if not folder_slug:
            return Response({"error": "Не указан slug папки"}, status=status.HTTP_400_BAD_REQUEST)
        target_folder = get_object_or_404(Folder, slug=folder_slug)
        message.folder = target_folder
        message.save(update_fields=['folder'])
        return Response({"status": "success", "message": f"Pисьмо перемещено в {target_folder.name}"})

    def destroy(self, request, *args, **kwargs):
        '''
        Метод удаления письма 
        '''
        instance = self.get_object()
        trash_folder = Folder.objects.filter(slug='trash').first()
        if instance.folder != trash_folder:
            if trash_folder:
                instance.folder = trash_folder
                instance.save(update_fields=['folder'])
                return Response({"status": "moved_to_trash"}, status=status.HTTP_200_OK)
        instance.is_deleted_permanently = True
        instance.save(update_fields=['is_deleted_permanently'])
        return super().destroy(request, *args, **kwargs)

class FolderViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    Контроллер для получения списка папок
    '''
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer