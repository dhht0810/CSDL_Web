from django.shortcuts import get_object_or_404, render
from .models import *
from django.utils import timezone

# Create your views here.
def home(request):
    mydata = story.objects.raw("select * from app_story")
    return render(request, 'app/home.html', {'story':mydata})

def list_category(request):
    mydata = category.objects.raw("select * from app_category")
    return {"category":mydata}

def search(request):
    search_story = request.GET['search_story']
    mydata = story.objects.raw("select * from app_story where name like %s",['%' + search_story + '%'])
    return render(request, 'app/search.html', context={'search_story':search_story, "story":mydata})
    
    
def list_story_category(request, id):
    myCategory = category.objects.raw("select * from app_category where id = %s",[id])
    myStory = story.objects.raw("select app_story.* from app_category join app_story_categories "
                               + "on app_category.id = category_id join app_story "
                               + "on app_story.id = story_id where app_category.id = %s",[id])
    list_category = category.objects.raw("select * from app_category")
    return render(request, 'app/category.html', {'story':myStory, 'category': myCategory, 'list_category': list_category})

def list_chapter(request, id):
    myChapter = chapters.objects.raw("select * from app_chapters where story_id = %s",[id])
    myStory = story.objects.raw("select * from app_story where id = %s",[id])
    myCategory = story.objects.raw("select app_category.* from app_category join app_story_categories "
                               + "on app_category.id = category_id join app_story "
                               + "on app_story.id = story_id where app_story.id = %s",[id])
    return render(request, 'app/story.html', {'chapters': myChapter, 'story': myStory, 'category': myCategory})

def chapter(request, story_id, chapter_id):
    myStory = story.objects.raw("select * from app_story where id = %s",[story_id])
    myChapter = chapters.objects.raw("select * from app_chapters where story_id = %s",[story_id])
    chapter = chapters.objects.raw("select * from app_chapters where story_id = %s and id = %s",[story_id, chapter_id])
    chaptertruoc= chapters.objects.raw("select * from app_chapters where story_id = %s and id = %s",[story_id, chapter_id-1])
    chaptersau = chapters.objects.raw("select * from app_chapters where story_id = %s and id = %s",[story_id, chapter_id+1])
    
    if request.method == "POST":
        comment_content = request.POST.get('comment')
        reply_content = request.POST.get('reply')
        get_object_or_404(comment, id=int(request.POST.get('delete'))).delete()
        if comment_content and comment_content.strip() != '':
            addComment = comment.objects.create(comments=comment_content,user=request.user,chapters_id=chapter_id)
            addComment.save()
        if reply_content and reply_content.strip() != '':
            parent_comment = get_object_or_404(comment, id=int(request.POST.get('hidden')))
            addReply = comment.objects.create(comments=reply_content,user=request.user,chapters_id=chapter_id,reply= parent_comment)
            addReply.save()
            
    myComment = comment.objects.raw("select * from app_comment where chapters_id = %s and reply_id is null", [chapter_id])    
    myReply = []
        
        
    file = chapter[0].file.open('r')

    return render(request, 'app/chapter.html', {'chapter': chapter, 'chaptertruoc': chaptertruoc, 'chaptersau': chaptersau, 
                                            'story': myStory, 'list_chapter': myChapter, 'data': file.read(), 'list_comment': myComment,
                                            })
