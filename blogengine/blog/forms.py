from typing import NewType
from django import forms
from django.db.models import fields
from .models import Post, Tag
from django.core.exceptions import ValidationError

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']
        labels = {
            'title':'Название'
        }

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Введите название тэга'}),
            'slug':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Введите slug'})
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
        labels = {
            'title': 'Название поста',
            'body': 'Текст поста',
            'tag':'Тэги поста'
        }

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Введите названиеп поста'}),
            'slug':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Введите slug'}),
            'body':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Введите текст поста'}),
            'tag':forms.CheckboxSelectMultiple(attrs={'class':'checkbox_tag'})
        }