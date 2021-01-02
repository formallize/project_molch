from .forms import PostForm, TagForm
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404

from .models import *

default_variables = [
    'model = None',
    'template = None'
]

default_variables_create = [
    'form = None',
    'template = None'
]

class ObjectDetailMixin:
    default_variables

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower():obj})

class ObjectListMixin:
    default_variables

    def get(self, request):
        if self.model == Post:
            obj = self.model.objects.all().order_by('-date_pub')
        else:
            obj = self.model.objects.all()

        return render(request, self.template, context={self.model.__name__.lower()+'s':obj})

class ObjectCreateMixin:
    default_variables_create

    def get(self, request):
        form = self.form()
        return render(request, self.template, context={'form':form})
    
    def post(self, request):
        bound_form = self.form(request.POST)

        if bound_form.is_valid():
            if self.form == PostForm:
                    bound_form.save()
                    return redirect('post_list')
            else:
                new_tag = bound_form.save()
                return redirect('tag_list')

        return render(request, self.template, context={'form': bound_form})