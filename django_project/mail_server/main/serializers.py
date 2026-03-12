from rest_framework import serializers
from .models import EmailMessage, Folder

class FolderSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для модели папок
    '''
    class Meta:
        '''
        Мета-класс сериализатора папок
        '''
        model = Folder
        fields = ['id', 'name', 'slug']

class EmailMessageSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для модели писем
    '''
    folder_name = serializers.CharField(source='folder.name', read_only=True)

    class Meta:
        '''
        Класс сериализатора писем
        '''
        model = EmailMessage
        fields = [
            'id', 'sender', 'recipient', 'subject', 'body', 
            'is_read', 'created_at', 'folder', 'folder_name'
        ]
        read_only_fields = ['id', 'created_at', 'folder_name']

    def create(self, validated_data):
        '''
        Метод создания нового письма
        '''
        if 'folder' not in validated_data:
            try:
                sent_folder = Folder.objects.get(slug='sent')
                validated_data['folder'] = sent_folder
            except Folder.DoesNotExist:
                raise serializers.ValidationError("Папка 'Отправленные' не найдена")
        return super().create(validated_data)