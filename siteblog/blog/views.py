# from django.http import HttpResponse
from django.db.models import F
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


class PostsByCategory(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False  # При запросе несуществующей категории будет ошибка 404

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        # context['title'] = self.kwargs['slug'].capitalize() # Тоже что и выше но без запроса к БД (правильно ли это?)
        return context


class GetPost(DetailView):
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # Увеличиваем количество просмотров и записываем в БД
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()  # Переобращаемся к БД и забираем обновленное поле views (если не написать, то вывод будет вида F(views) + Value(1)
        return context


class PostsByTag(ListView):
    template_name = 'blog/category.html'  # Используем тот-же шаблон что и для категорий, т.к. все одно и тоже, только заменим Title на странице
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False  # При запросе несуществующей категории будет ошибка 404

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Posts by tag: '+ str(Tag.objects.get(slug=self.kwargs['slug']))
        return context

class Search(ListView):
    template_name = 'blog/search.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"  # Чтобы работала пагинация на странице результатов поиска, см. урок 16
        context['s_phrase'] = self.request.GET.get('s')
        return context

# def index(request):
#     return render(request, 'blog/index.html')

# def get_category(request, slug):
#     return render(request, 'blog/category.html', {'slug': slug})
