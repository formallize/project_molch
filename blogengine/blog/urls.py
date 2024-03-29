from django import urls
from django.urls import path
from .views import *


urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post/create', PostCreate.as_view(), name='post_create'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail'),
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update'),
    path('post/<str:slug>/delete/', PostDelete.as_view(), name='post_delete'),
    path('tags/', TagList.as_view(), name='tag_list'),
    path('tag/create', TagCreate.as_view(), name='tag_create'),
    path('tag/<str:slug>', TagDetail.as_view(), name='tag_detail'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update'),
    path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete')
]
