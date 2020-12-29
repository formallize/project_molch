from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import get_object_or_404

from .models import *


def post_list(requset):
    posts = Post.objects.all()
    return render(requset, 'blog/index.html', context={'posts':posts})

# def post_detail(request, slug):
#   post = Post.objects.get(slug__iexact=slug)
#    return render(request, 'blog/post_detail.html', context={'post':post})

class PostDetail(View):
    def get(self, request, slug):
        #post = Post.objects.get(slug__iexact=slug)
        post = get_object_or_404(Post, slug__iexact=slug)
        return render(request, 'blog/post_detail.html', context={'post':post})

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tag_list.html', context={'tags':tags})

class TagDetail(View):
    def get(self, request, slug):
        #tags = Tag.objects.all()
        tag = get_object_or_404(Tag, slug__iexact=slug)
        return render(request, 'blog/tag_detail.html', context={'tag':tag})

#def tag_detail(request, slug):
#    tag = Tag.objects.get(slug__iexact=slug)
#    return render(request, 'blog/tag_detail.html', context={'tag':tag})