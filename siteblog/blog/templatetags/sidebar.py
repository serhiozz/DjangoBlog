'''
Модуль темплейт тега для вывода тегов в сайдбаре справа
'''
from django import template
from blog.models import Tag, Post


register = template.Library()

@register.inclusion_tag('blog/popular_posts_tpl.html')
def get_popular(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt] # Получаем популярные поcты по количеству просмотров в количестве cnt
    return {'posts': posts}

@register.inclusion_tag('blog/tags_tpl.html')
def get_tags():
    tags = Tag.objects.all()
    return {'tags': tags}
