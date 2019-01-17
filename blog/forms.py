from django import forms
from django.contrib.auth.models import User

from blog.models import Article

class AddarticleFormView(forms.ModelForm):

    class Meta:
        model = Article
        fields = (
            'title',
            'content',
            'article_image'
        )
