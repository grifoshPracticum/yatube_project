from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница')


# Страница со списком мороженого
def group_list(request, slug):
    return HttpResponse(f'Группа: {slug}')


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def post_detail(request, pk):
    return HttpResponse(f'Пост номер {pk}')