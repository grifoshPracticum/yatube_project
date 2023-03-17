from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from posts.models import Post, Group


# Главная страница
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    string = 'Это кусочек текста, который вставлен в шаблоне через переменную'
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)

def group_posts(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)
def group_detail(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


def post_list(request):
    return HttpResponse(f'Посты')
def post_detail(request, pk):
    return HttpResponse(f'Пост номер: {pk}')

def user_detail(request, id):
    return HttpResponse(f'Профиль пользователя: {id}')