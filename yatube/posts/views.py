from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


# Главная страница
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_list(request):
    return HttpResponse(f'Группа: {slug}')
def group_detail(request, slug):
    return HttpResponse(f'Группа: {slug}')


def post_list(request):
    return HttpResponse(f'Посты')
def post_detail(request, pk):
    return HttpResponse(f'Пост номер: {pk}')

def user_detail(request, id):
    return HttpResponse(f'Профиль пользователя: {id}')