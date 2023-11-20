from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('search/', search, name='search'),
    path('category/<int:id>/', list_story_category, name='category'),
    path('story/<int:id>', list_chapter, name='story'),
    path('story/<int:story_id>/chapter/<int:chapter_id>', chapter, name='chapter'),
    path('author/<int:id>/', list_story_author, name='author'),
    path('history/',history,name='history'),
    path('danhsach/<str:name>',danhsach,name='danhsach'),
]
