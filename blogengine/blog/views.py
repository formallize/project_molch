from django.views.generic import View

from .models import *
from .utils import *


class PostList(ObjectListMixin, View):
    model = Post
    template = 'blog/index.html'

class TagList(ObjectListMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'
