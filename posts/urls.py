from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_posts, name='feed'),
    path('posts/new', views.create_post, name='create_post')
]
