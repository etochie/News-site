from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views import View

from .models import *


def index(request):
    search_query = request.GET.get('search', '')
    if search_query:
        articles = Article.objects.filter(
            Q(title__icontains=search_query) | Q(title2__icontains=search_query) | Q(body__icontains=search_query)
        )
    else:
        articles = Article.objects.all()
    tags = Tag.objects.all()
    return render(request, 'news/index.html', context={'articles': articles, 'tags': tags})


# def article_detail(request, slug):
#     obj = get_object_or_404(Article, slug__iexact=slug)
#     return render(request, 'news/article_detail.html', context={'article': obj})


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(request, 'news/tag_detail.html', context={'tag': tag})


# def article_list(request, slug):
#     article = get_object_or_404(Article, slug__iexact=slug)
#     context = {}
#
#     obj, created = ArticleStatistic.objects.get_or_create(
#         defaults=
#     )

# class ArticleView(View):
#     template_name = 'news/article_list.html'
#
#     def get(self, request, slug):
#         article = get_object_or_404(Article, slug__iexact=slug)
#         context = {}
#
#         obj, created = ArticleStatistic.objects.get_or_create(
#             defaults={
#                 'article': article,
#                 'date': timezone.now()
#             }
#         )
#         obj.views += 1
#         obj.save(update_fields=['views'])
#
#         popular = ArticleStatistic.objects.filter(
#             date__range=[timezone.now() - timezone.timedelta(days=7), timezone.now()]
#         ).values(
#             'article__slug', 'article__title'
#         ).order_by('-views')[:5]
#
#         context['popular_list'] = popular
#
#         return render(request, template_name=self.template_name, context=context)


# def article_detail(request, slug):
#     article = get_object_or_404(Article, slug__iexact=slug)
#
#     obj, created = ArticleStatistic.objects.get_or_create(article=article, date=timezone.now())
#     obj.views += 1
#     obj.save(update_fields=['views'])
#
#     return render(request, template_name='news/article_detail.html', context={'article': article, 'obj': obj})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug__iexact=slug)
    article.views += 1
    article.save(update_fields=['views'])

    obj, created = ArticleStatistic.objects.get_or_create(article=article, date=timezone.now())
    obj.views += 1
    obj.save(update_fields=['views'])

    return render(request, template_name='news/article_detail.html', context={'article': article})

