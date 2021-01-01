from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import *

default_variables = [
    'model = None',
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
        obj = self.model.objects.all()

        if self.model == 'Post':
            obj = obj.ordering('-date_pub')

        return render(request, self.template, context={self.model.__name__.lower()+'s':obj})
