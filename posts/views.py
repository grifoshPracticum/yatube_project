from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Post


# Главная страница
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    string = 'Это кусочек текста, который вставлен в шаблоне через переменную'
    context = {
        'posts': posts,
        'string': string ,
    }
    return render(request, 'base.html', context)

def group_posts(request):
    return HttpResponse(f'Здесь будет информация о группах проекта Yatube')
def group_detail(request, slug):
    return HttpResponse(f'Группа: {slug}')


def post_list(request):
    return HttpResponse(f'Посты')
def post_detail(request, pk):
    return HttpResponse(f'Пост номер: {pk}')

def user_detail(request, id):
    return HttpResponse(f'Профиль пользователя: {id}')