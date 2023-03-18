from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from posts.models import Post, Group


# Главная страница
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)

def groups(request):
    pass


def group(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


def post(request, pk):
    return HttpResponse(f'Пост номер: {pk}')
