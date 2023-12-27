from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime

class NewsList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["time_now"] = datetime.utcnow()
        return context
    
    
class News_content(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'news_content.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'news'

