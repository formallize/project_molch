from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date_pub')
    list_filter = ('title', 'slug', 'tag')
    prepopulated_fields = {'slug':('title',)}
