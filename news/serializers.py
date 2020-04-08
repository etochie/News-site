from rest_framework import serializers

from .models import Article, Tag


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('__all__')


class TagSerializer(serializers.ModelSerializer):
    posts = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = ('__all__')
