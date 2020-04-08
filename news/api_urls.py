from django.urls import path
# from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

from news import api_views


schema_view = get_swagger_view(title='News-site-API')

urlpatterns = [

    path('articles/', api_views.ArticleListCreateView.as_view(), name='article_list_create_url'),
    path('articles/<int:pk>/', api_views.ArticleDetailView.as_view(), name='article_detail_url'),
    path('tags/', api_views.TagListCreateView.as_view(), name='tag_list_create_url'),
    path('tags/<int:pk>/', api_views.TagDetailView.as_view(), name='tag_detail_url'),
    path('docs/', schema_view)

]
