from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    # path('category/<str:slug>/', get_category, name='category'),
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('post/<str:slug>/', get_post, name='post')
]