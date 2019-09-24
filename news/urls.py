from django.urls import path

from news import views

app_name = 'news'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:slug>/', views.article_detail, name='article_detail_url')
]