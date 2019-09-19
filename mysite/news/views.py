from django.shortcuts import render, get_object_or_404
from .models import *

def index(request):
    articles = Article.objects.all()
    return render(request, 'news/index.html', context={'articles': articles})

def article_detail(request, slug):
    obj = get_object_or_404(Article, slug__iexact=slug)
    return render(request, 'news/article_detail.html', context={'article': obj})

