from django.shortcuts import render, get_object_or_404
from .models import *

def index(request):
    articles = Article.objects.all()
    tags = Tag.objects.all()
    return render(request, 'news/index.html', context={'articles': articles, 'tags': tags})

def article_detail(request, slug):
    obj = get_object_or_404(Article, slug__iexact=slug)
    return render(request, 'news/article_detail.html', context={'article': obj})

def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(request, 'news/tag_detail.html', context={'tag': tag})


