from time import time

from django.db import models
from django.utils import timezone
from django.shortcuts import reverse

from pytils.translit import slugify


def gen_slug(text):
    new_slug = slugify(text)
    time_slug = str(int(time()))
    return new_slug + '-' + time_slug


# def gen_img_name(old_name, new_name):
#     new_split = old_name.split('.')  # разделяем расширение от названия
#     extension = new_split[1]  # расширение
#     new_gen_name = slugify(new_name)
#     return new_gen_name + '.' + extension


class Article(models.Model):
    title = models.CharField(max_length=200)
    title2 = models.CharField(max_length=300, blank=True)
    img = models.ImageField(blank=True)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    body = models.TextField()
    tag = models.ManyToManyField('Tag', blank=True, related_name='posts')
    pub_date = models.DateTimeField(default=timezone.now, blank=False)
    views = models.IntegerField('Просмотры', default=0)

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


class ArticleStatistic(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date = models.DateField('Дата', default=timezone.now)
    views = models.IntegerField('Просмотры', default=0)

    class Meta:
        db_table = 'ArticleStatistic'

    def __str__(self):
        return self.article.title


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_detail_url(self):
        return reverse('news:tag_detail_url', kwargs={'slug': self.slug})
