from django.contrib import admin

from blog.models import Article, Comment, Tag

admin.site.register(Article)
admin.site.register(Tag)