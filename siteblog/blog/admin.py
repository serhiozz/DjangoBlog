from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}  # Автозаполнение поля Slug из значения Title

    list_display = ('id', 'title', 'slug')  # Отображаемые поля в списке
    list_display_links = ('id', 'title')  # id и заголовок в виде ссылке в админке в списке
    search_fields = ('title',)  # Возможность поиска по названию статьи


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    list_display = ('id', 'title', 'slug')  # Отображаемые поля в списке
    list_display_links = ('id', 'title')  # id и заголовок в виде ссылке в админке в списке
    search_fields = ('title',)  # Возможность поиска по названию статьи


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), label="Текст")

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    prepopulated_fields = {'slug': ('title',)}  # Создает слаг из заголовка

    save_as = True  # Добавляет кнопку для быстрого заполения новой новости на основе предыдущей
    save_on_top = True  # Дублирует кнопки сохранения в верху страницы

    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'get_photo', 'views')  # Отображаемые поля в списке
    list_display_links = ('id', 'title')  # id и заголовок в виде ссылке в админке в списке
    list_filter = ('category',)  # Добавляет возможность фильтрации статей по категории
    search_fields = ('title',)  # Возможность поиска по названию статьи

    readonly_fields = ('views', 'created_at', 'get_photo')  # Поля "только для просмотра"
    fields = ('title', 'slug', 'category', 'tags', 'content', 'photo', 'get_photo', 'views', 'created_at')  # Отображаемые поля в статье

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50"/>')
        return "No photo"

    get_photo.short_description = "Фото"  # Описание столбца в админке


# Регистрируем в админку
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
