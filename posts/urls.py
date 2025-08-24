from django.urls import path
from .views import post_detail, post_list

urlpatterns = [
    path('posts/<int:post_id>/', post_detail, name='post_detail'),
    path('posts/', post_list, name='post_list'),
]
