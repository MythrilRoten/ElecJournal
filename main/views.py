from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from .models import *


menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Обратная связь", 'url_name': 'feedback'},
    {'title': "Табель успеваемости", 'url_name': 'grades'},
    {'title': "Распечатка рапортов", 'url_name': 'print'},
    {'title': "Войти", 'url_name': 'login'},
]


def index(request):
    posts = News.objects.all()
    
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    
    return render(request, 'main/index.html', context=context)

def about(request):
    return render(request, 'main/about.html', {'menu': menu, 'title': 'О сайте'})

def table_grades(request):
    return HttpResponse('Табель оценок')

def printout(request):
    return HttpResponse('Заполнение и распечатка рапортов')

def login(request):
    return HttpResponse('Логин')

def contact(request):
    return HttpResponse('Контакты')

def show_post(request, post_id):
    post = get_object_or_404(News, pk=post_id)
    
    context = {
        'posts': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.categ_id,
    }
    
    return render(request, 'main/post.html', context=context)

def show_category(request, cat_id):
    posts = News.objects.filter(categ_id=cat_id)
    
    if len(posts) == 0:
        raise Http404()
    
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по категориям',
        'cat_selected': cat_id,
    }
    
    return render(request, 'main/index.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')

