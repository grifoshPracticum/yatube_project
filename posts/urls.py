from django.urls import path
from posts import views

app_name = 'posts'

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
    path('post/<pk>/', views.post_detail, name='post_detail'),
    ]