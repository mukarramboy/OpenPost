from django.urls import path
from .views import post_detail, post_list, add_comment, like_comment,user_login, user_logout, signup

urlpatterns = [
    path('posts/<int:pk>/', post_detail, name='post_detail'),
    path('posts/', post_list, name='post_list'),
    path('posts/<int:pk>/comment/', add_comment, name='add_comment'),
    path('comments/<int:pk>/like/', like_comment, name='like_comment'),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("signup/", signup, name="signup"),
]
