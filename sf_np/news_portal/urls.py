from django.contrib import admin
from django.urls import path
from .views import NewsList, News_content

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>/', News_content.as_view())
]