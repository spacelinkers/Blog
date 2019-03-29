from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView,DetailView
from django.contrib.auth.models import User

from blog.models import Article
from blog.forms import AddarticleFormView

class ArticlesView(TemplateView):
    template_name = 'blog/articles.html'
    
    def get(self, request):
        articles = Article.objects.all().order_by('-create_date')
        users = User.objects.all()
        context = {
            'articles': articles,
            'users': users
        }
        return render(request, self.template_name, context)
    

class DashboardView(DetailView):
    template_name = 'blog/dashboard.html'
    
    def get(self, request):
        context = {
            'user': request.user,
        }
        return render(request, self.template_name, context)

class AddarticleView(TemplateView):
    template_name = 'blog/addarticle.html'

    def get(self, request):
        form = AddarticleFormView()
        context = {
            'form': form, 
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = AddarticleFormView(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()

            return redirect('blog:dashboard')
    
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)



class ArticleView(DetailView):
    template_name = 'blog/article.html'
    
    def get(self, request, id):
        articles = get_object_or_404(Article,id = id)
        context = {
            'article': articles,
        }
        return render(request, self.template_name, context)
    
class UpdateView(TemplateView):
    template_name = 'blog/update.html'

class DeleteView(TemplateView):
    template_name = 'blog/delete.html'

class CommentView(TemplateView):
    template_name = 'blog/comment.html'