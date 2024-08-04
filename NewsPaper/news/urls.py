
from django.urls import path, include
from .views import (NewsCreateView, NewsUpdateView, NewsDeleteView,
                    ArticleCreateView, ArticleUpdateView, ArticleDeleteView)
from .forms import NewsForm, ArticleForm

urlpatterns = [

    path('news/create/',NewsCreateView.as_view(form_class=NewsForm), name='news_create'),
    path('news/<int:pk>/edit/', NewsUpdateView.as_view(form_class=NewsForm), name='news_update'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('news/', include('news')),

    path('articles/create/', ArticleCreateView.as_view(form_class=ArticleForm), name='article_create'),
    path('articles/<int:pk>/edit/', ArticleUpdateView.as_view(form_class=ArticleForm), name='article_update'),
    path('articles/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
]