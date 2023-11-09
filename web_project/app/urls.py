from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('search/', search, name='search'),
    path('category/<int:id>/', list_story_category, name='category'),
    path('story/<int:id>/', list_chapter, name='story'),
    path('story/<str:story_id>/chapter/<int:id>', chapter, name='chapter'),
]
