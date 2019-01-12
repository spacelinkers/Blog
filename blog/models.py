from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Article(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'author')
    title = models.CharField(max_length = 50, verbose_name = 'Title')
    content = RichTextField()
    create_date = models.DateTimeField(auto_now_add = True, verbose_name = 'Date Created')
    article_image = models.ImageField(upload_to = 'blog_cover', blank = True, null = True, verbose_name = 'Add Cover Photo')

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-create_date']

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE, verbose_name = 'Article', related_name = 'comment')
    comment_author = models.CharField(max_length = 50, verbose_name = 'Post Name')
    comment_content = models.CharField(max_length = 200, verbose_name = 'content')
    comment_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.comment_content
    
    class Meta:
        ordering = ['comment_date']

