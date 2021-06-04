from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('posts/', views.list_posts, name='feed'),
]
