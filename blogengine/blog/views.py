from django.core.exceptions import RequestDataTooBig
from django.shortcuts import redirect
from django.views.generic import View
from .forms import PostForm, TagForm

from .models import *
from .utils import *


class PostList(ObjectListMixin, View):
    model = Post
    template = 'blog/index.html'

class TagList(ObjectListMixin, View):
    model = Tag
    template = 'blog/tag_list.html'

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'

class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create.html', context={'form':form})
    
    def post(self, request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'blog/tag_create.html', context={'form':bound_form})

class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_create.html', context={'form':form})

    def post(self, request):
        bound_form = PostForm(request.POST)

        if bound_form.is_valid():
            bound_form.save()
            return redirect('post_list')
        return render(request, 'blog/post_create.html', context={'form':bound_form})