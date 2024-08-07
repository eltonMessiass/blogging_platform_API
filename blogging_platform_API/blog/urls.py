from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.ArticleView.as_view(), name="articles"),
    path('articles/<int:pk>/', views.ArticleDetailView.as_view(), name="article_detail"),
    path('tags', views.TagView.as_view(), name="tags"),
    # path('articles/filter_by_tags/', views.ArticlesFilterByTags ,name='articles_filter_by_tags'),
]