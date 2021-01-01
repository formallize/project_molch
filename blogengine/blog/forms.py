from typing import NewType
from django import forms
from django.db.models import fields
from .models import Post, Tag
from django.core.exceptions import ValidationError

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'slug':forms.TextInput(attrs={'class':'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug не может называться "Create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Данный слаг должен быть уникальным. Уже есть slug - "{}"'.format(new_slug))
        return new_slug

 
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tag']

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'slug':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'tag':forms.CheckboxSelectMultiple(attrs={'style': {'list-style-type':'none'}})
        }