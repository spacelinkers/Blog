from django.urls import path, re_path

from blog.views import (
    ArticlesView, DashboardView, AddarticleView,
    ArticleView, UpdateView, DeleteView, CommentView,
    TagView, 
)

app_name = 'blog'
urlpatterns = [
    re_path(r'^$', ArticlesView.as_view(), name = 'articles'),
    re_path(r'^(?P<id>\d+)/$',TagView.as_view(), name = 'tag'),
    re_path(r'^dashboard/$', DashboardView.as_view(), name = 'dashboard'),
    re_path(r'^addarticle/$', AddarticleView.as_view(), name = 'addarticle'),
    re_path(r'^article/(?P<id>\d+)/$', ArticleView.as_view(), name = 'article'),
    re_path(r'^update/(?P<id>\d+)/$', UpdateView.as_view(), name = 'update'),
    re_path(r'^delete/(?P<id>\d+)/$', DeleteView.as_view(), name = 'delete'),
    re_path(r'^comment/(?P<id>\d+)/$', CommentView.as_view(), name = 'comment'),

]