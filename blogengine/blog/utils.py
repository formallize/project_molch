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
            bound_form.save()
            return redirect(self.model.__name__.lower()+'_list')
        return render(request, self.template, context={'form': bound_form})

class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        return render(request, self.template, context={'form':bound_form, self.model.__name__.lower():obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(request.POST, instance=obj)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(reverse(self.model.__name__.lower()+'_list'))
        return render(request, self.template, context={'form':bound_form, self.model.__name__.lower():obj})

class ObjectDeleteMixin:
    default_variables

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower():obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.model.__name__.lower()+'_list'))
