from django import urls
from django.urls import path
from .views import *


urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail'),
    path('tags/', TagList.as_view(), name='tag_list'),
    path('tag/create', TagCreate.as_view(), name='tag_create'),
    path('tag/<str:slug>', TagDetail.as_view(), name='tag_detail')
]
