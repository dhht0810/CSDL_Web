import os
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import *

# Create your views here.
def home(request):
    mydata = story.objects.raw("select * from app_story")
    return render(request, 'home.html', {'story':mydata})

def list_category(request):
    mydata = category.objects.raw("select * from app_category")
    return {"category":mydata}

def search(request):
    search_story = request.GET['search_story']
    mydata = story.objects.raw("select * from app_story where name like %s",['%' + search_story + '%'])
    return render(request, 'search.html', context={'search_story':search_story, "story":mydata})
    
    
def list_story_category(request, id):
    myCategory = category.objects.raw("select * from app_category where id = %s",[id])
    myStory = story.objects.raw("select app_story.* from app_category join app_story_categories "
                               + "on app_category.id = category_id join app_story "
                               + "on app_story.id = story_id where app_category.id = %s",[id])
    list_category = category.objects.raw("select * from app_category")
    return render(request, 'category.html', {'story':myStory, 'category': myCategory, 'list_category': list_category})

def list_chapter(request, id):
    myChapter = chapters.objects.raw("select * from app_chapters where story_id = %s",[id])
    myStory = story.objects.raw("select * from app_story where id = %s",[id])
    myCategory = story.objects.raw("select app_category.* from app_category join app_story_categories "
                               + "on app_category.id = category_id join app_story "
                               + "on app_story.id = story_id where app_story.id = %s",[id])
    return render(request, 'story.html', {'chapters': myChapter, 'story': myStory, 'category': myCategory})

def chapter(request, story_id, id):
    myStory = story.objects.raw("select * from app_story where id = %s",[story_id])
    myChapter = chapters.objects.raw("select * from app_chapters where story_id = %s",[story_id])
    chapter = chapters.objects.raw("select * from app_chapters where story_id = %s and id = %s",[story_id, id])
    chaptertruoc= chapters.objects.raw("select * from app_chapters where story_id = %s and id = %s",[story_id, id-1])
    chaptersau = chapters.objects.raw("select * from app_chapters where story_id = %s and id = %s",[story_id, id+1])
    file = chapter[0].file.open('r')
    data = ""
    for x in file:
        data += x
    file.close()
    return render(request, 'chapter.html', {'chapter': chapter, 'chaptertruoc': chaptertruoc, 'chaptersau': chaptersau, 
                                            'story': myStory, 'list_chapter': myChapter, 'data': data})
