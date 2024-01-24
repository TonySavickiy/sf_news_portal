from django.contrib import admin
from django.urls import path
from .views import NewsList, News_content, SearchList, PostDelete, PostNewsAdd, PostUpdate, CategoryList, PostArticleAdd

urlpatterns = [
    path('', NewsList.as_view(), name='home'),
    path('<int:pk>/', News_content.as_view(), name='post_detail'),
    path('search/', SearchList.as_view(), name='search'),
    path('news/create/', PostNewsAdd.as_view(), name='post_create'),
    path('news/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('article/create/', PostArticleAdd.as_view(), name='post_article_create'),
    path('article/<int:pk>/update/', PostUpdate.as_view(), name='post_article_update'),
    path('article/<int:pk>/delete/', PostDelete.as_view(), name='post_article_delete'),
    path('categories/<int:pk>', CategoryList.as_view(), name='category_list'),
]