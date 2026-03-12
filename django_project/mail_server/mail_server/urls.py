from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main.views import EmailMessageViewSet, FolderViewSet

router = DefaultRouter()
router.register(r'messages', EmailMessageViewSet, basename='message')
router.register(r'folders', FolderViewSet, basename='folder')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
