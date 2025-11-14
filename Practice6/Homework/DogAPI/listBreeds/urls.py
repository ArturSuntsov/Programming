from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_breeds, name='list_breeds'),
    path('images/', views.breeds_images, name='breeds_images')
]