'''
Модуль тега для шаблонов вернего и нижнего меню сайта
menu_class - класс меню (header, footer)
'''
from django import template
from blog.models import Category


register = template.Library()

@register.inclusion_tag('blog/menu_tpl.html')
def show_menu(menu_class='menu'):
    categories = Category.objects.all()
    return {'categories': categories, 'menu_class': menu_class}

