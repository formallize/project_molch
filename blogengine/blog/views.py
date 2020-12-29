from django.shortcuts import render
from .models import Post


def post_list(requset):
    posts = Post.objects.all()
    return render(requset, 'blog/index.html', context={'posts':posts})

def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post':post})