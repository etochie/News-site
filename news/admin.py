from django.contrib import admin

from .models import Article, Tag, ArticleViews


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
         {'fields': ['title', 'title2', 'img', 'body', 'tag']}),
        ('Date information',
         {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('__str__', 'pub_date', 'views')


class TagAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
         {'fields': ['title', 'slug']})
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(ArticleViews)
