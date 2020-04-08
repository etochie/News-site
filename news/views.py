from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Article, Tag, ArticleViews


def index(request):
    search_query = request.GET.get('search', '')
    if search_query:
        articles = Article.objects.filter(
            Q(title__icontains=search_query)
            | Q(title2__icontains=search_query)
            | Q(body__icontains=search_query))
    else:
        articles = Article.objects.all()
    tags = Tag.objects.all()
    return render(request,
                  'news/index.html',
                  context={
                      'articles': articles,
                      'tags': tags
                  })


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(request, 'news/tag_detail.html', context={'tag': tag})


def article_detail(request, slug):
    article = get_object_or_404(Article, slug__iexact=slug)

    # проверяем есть ли модель отслеживания
    if not ArticleViews.objects.filter(article=article,
                                       session=request.session.session_key):
    # если нет, создаем её, забирая из request нужные данные 
        view = ArticleViews(
            article=article,
            ip=request.META['REMOTE_ADDR'],
            session=request.session.session_key,
        )
        view.save()

    return render(request,
                  template_name='news/article_detail.html',
                  context={'article': article})
