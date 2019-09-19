from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
         {'fields': ['title', 'title2', 'img', 'body']}),
        ('Date information',
         {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

admin.site.register(Article, ArticleAdmin)
