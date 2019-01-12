from django.urls import path

from blog.views import (
    ArticlesView, DashboardView, AddarticleView,
    ArticleView, UpdateView, DeleteView, CommentView,
)

app_name = 'blog'
urlpatterns = [
    path('', ArticlesView.as_view(), name = 'articles'),
    path('dashboard/', DashboardView.as_view(), name = 'dashboard'),
    path('addarticle/', AddarticleView.as_view(), name = 'addarticle'),
    path('article/<int:id>', ArticleView.as_view(), name = 'article'),
    path('update/<int:id>/', UpdateView.as_view(), name = 'update'),
    path('delete/<int:id>/', DeleteView.as_view(), name = 'delete'),
    path('comment/<int:id>/', CommentView.as_view(), name = 'comment'),

]