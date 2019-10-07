from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import *


def index(request):
    search_query = request.GET.get('search', '')
    if search_query:
        articles = Article.objects.filter(Q(title__icontains=search_query) | Q(title2__icontains=search_query) | Q(body__icontains=search_query))
    else:
        articles = Article.objects.all()
    tags = Tag.objects.all()
    return render(request, 'news/index.html', context={'articles': articles, 'tags': tags})


def article_detail(request, slug):
    obj = get_object_or_404(Article, slug__iexact=slug)
    return render(request, 'news/article_detail.html', context={'article': obj})


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(request, 'news/tag_detail.html', context={'tag': tag})
