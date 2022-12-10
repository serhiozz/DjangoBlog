# from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


#  Главная страница
class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4

    #  Функция для передачи данных в шаблон (title)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic blog design'
        return context


# def index(request):
#     return render(request, 'blog/index.html')


def get_category(request, slug):
    return render(request, 'blog/category.html', {'slug': slug})


def get_post(request, slug):
    return render(request, 'blog/category.html', {'slug': slug})
