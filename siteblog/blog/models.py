from django.db import models
from django.urls import reverse

"""
Category
============
title, slug

Tag
============
title, slug

Post
===========
title, slug, content, author, published, created_at, photo, views, category, tags
"""


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Категория')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})  # Для формирования ссылок см. urls.py

    class Meta:
        ordering = ['title']  # сортировка
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тег')
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})  # Для формирования ссылок см. urls.py

    class Meta:
        ordering = ['title']
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    author = models.CharField(max_length=100, verbose_name='Автор')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Pic')
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts', verbose_name='Теги')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})  # Для формирования ссылок см. urls.py

    class Meta:
        ordering = ['-created_at']   # сортировка в обратном порядке (самые свежие выше)
        verbose_name = "Новость"
        verbose_name_plural = "Новости"