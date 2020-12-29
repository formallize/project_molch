from django import urls
from django.urls import path
from .views import *


urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<str:slug>/', post_detail, name='post_detail'),
    path('tags/', tag_list, name='tag_list'),
    path('tag/<str:slug>', tag_detail, name='tag_detail')
]