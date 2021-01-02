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

class TagCreate(ObjectCreateMixin, View):
    form = TagForm
    template = 'blog/tag_create.html'

class PostCreate(ObjectCreateMixin, View):
    form = PostForm
    template = 'blog/post_create.html'
