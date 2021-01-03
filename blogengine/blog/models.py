from django.db import models
from django.shortcuts import reverse

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    tag = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_pub = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('post_update', kwargs={'slug':self.slug})
    
    def get_delete_url(self):
        return reverse('post_delete', kwargs={'slug':self.slug})

    def __str__(self):
        return '{}'.format(self.title)
    
    
class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('tag_update', kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('tag_delete', kwargs={'slug':self.slug})