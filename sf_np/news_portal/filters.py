import django_filters
from django.forms import DateInput
from django_filters import FilterSet
from .models import Post, Category, PostCategory
       
NEWS = 'NW'
ARTICLE = 'AR'
CATEGORY_CHOICES = [
    (NEWS, 'Новость'),
    (ARTICLE, 'Статья')
]


#По заданию фильтр на три показателя(категория, заголовок и дата)
class NewsFilter(FilterSet):
    categoryType = django_filters.ChoiceFilter(label='Тип',choices=CATEGORY_CHOICES)
    title = django_filters.CharFilter(label='Заголовок', lookup_expr='icontains',)
    dateCreation = django_filters.DateFilter(widget=DateInput(attrs={'type': 'date'}),lookup_expr='gt',label='Даты поста')#По заданию больше чем указанная дата
    
    
    class Meta:
        model = Post
        fields = ['title','categoryType','dateCreation',]