from time import time

from django.db import models
from django.utils import timezone
from django.shortcuts import reverse

from pytils.translit import slugify


def gen_slug(text):
    new_slug = slugify(text)
    time_slug = str(int(time()))
    return new_slug + '-' + time_slug


class Article(models.Model):
    title = models.CharField(max_length=200)
    title2 = models.CharField(max_length=300, blank=True)
    img = models.ImageField(blank=True)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    body = models.TextField()
    tag = models.ManyToManyField('Tag', blank=True, related_name='posts')
    pub_date = models.DateTimeField(default=timezone.now, blank=False)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:  # сохранение сгенерированного slug
            self.slug = gen_slug(self.title[:20])
        # if self.img:
        #     name = gen_img_name(self.img.name, self.title[15])
        #     self.img.name = name
        return super().save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('news:article_detail_url', kwargs={'slug': self.slug})

    def get_pub_date(self):
        year = self.pub_date.year
        month = self.pub_date.month
        day = self.pub_date.day
        date = [year, month, day]
        return date

    def get_views(self):
        # костыльным методом определяем количество просмотров статьи
        queryset = ArticleViews.objects.filter(article=self) # фильтр по объектам, содержащих self статью
        views = len(queryset) # количество статей в списке ¯\_(ツ)_/¯
        return views


class ArticleViews(models.Model):
    """Модель для статистики просмотров статей

    Поля:
        article -- связь со статьей
        ip -- ip пользователя из request
        session -- session из request
        created -- дата и время последнего(!) просмотра статьи
    """
    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE,
                                related_name='views')
    ip = models.CharField(max_length=40)
    session = models.CharField(max_length=40)
    created = models.DateTimeField(verbose_name='last_view', auto_now=True)

    def __str__(self):
        return '{} | {}'.format(self.article.title, self.ip)


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_detail_url(self):
        return reverse('news:tag_detail_url', kwargs={'slug': self.slug})
