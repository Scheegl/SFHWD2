from django.contrib import admin
from .models import Category, Comment, Post, PostCategory

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(PostCategory)