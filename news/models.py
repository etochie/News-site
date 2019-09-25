from django.db import models
from django.utils import timezone
from django.shortcuts import reverse

from pytils.translit import slugify
from time import time


def gen_slug(s):
    new_slug = slugify(s)
    time_slug = str(int(time()))
    return new_slug + '-' + time_slug


# def gen_img_name(s):
#     img_name = slugify(s)
#     return img_name + '.jpg'


class Article(models.Model):
    title = models.CharField(max_length=200)
    title2 = models.CharField(max_length=300, blank=True)
    img = models.ImageField(blank=True)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    body = models.TextField()
    tag = models.ManyToManyField('Tag', blank=False, related_name='posts')
    pub_date = models.DateTimeField(default=timezone.now, blank=False)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title[:20])
        # if self.img:
        #     name = gen_img_name(self.title[:15])
        #     self.img.name = name
        return super().save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('news:article_detail_url', kwargs={'slug': self.slug})


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_detail_url(self):
        return reverse('news:tag_detail_url', kwargs={'slug': self.slug})


