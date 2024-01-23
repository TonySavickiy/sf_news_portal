from django.contrib import admin
from django.urls import path
from .views import NewsList, News_content, SearchList, PostDelete, PostAdd, PostUpdate, CategoryList

urlpatterns = [
    path('', NewsList.as_view(), name='home'),
    path('<int:pk>/', News_content.as_view(), name='post_detail'),
    path('search/', SearchList.as_view(), name='search'),
    path('create/', PostAdd.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('categories/<int:pk>', CategoryList.as_view(), name='category_list'),
]