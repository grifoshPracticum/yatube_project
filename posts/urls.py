from django.urls import path
from posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('groups/', views.groups, name='groups'),
    path('<pk>/', views.post, name='post'),
    path('group/<slug:slug>', views.group, name='group'),

    ]