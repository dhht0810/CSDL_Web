from django.shortcuts import get_object_or_404, redirect, render
from .models import *
import PyPDF2
import fitz

# Create your views here.

def home(request):
    mydata = story.objects.raw("select * from app_story")
    return render(request, 'app/home.html', {'story':mydata})

def list_category(request):
    mydata = category.objects.raw("select * from app_category")
    myStatus = ["HT","DCN",]
    if request.user.is_authenticated:
        user_stories = UserStory.objects.filter(user=request.user,follow=True,chapter__isnull=False,read=False).order_by('-date')
        return {"category":mydata, "status": myStatus,'notifications':user_stories,}
    return {"category":mydata, "status": myStatus,}

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
    myAuthors = author.objects.raw("select app_author.* from app_author join app_story_authors "
                               + "on app_author.id = author_id join app_story "
                               + "on app_story.id = story_id where app_story.id = %s",[id])
    user_story = get_object_or_404(story, id=id)
    if request.method == "POST":
        if 'unfollow' in request.POST:
            UserStory.objects.filter(user=request.user, story=user_story,follow=True).delete()
        elif 'follow' in request.POST:
            UserStory.objects.create(user=request.user, story=user_story,follow=True).save()
        return redirect("/story/" + str(id))
    
    is_following = UserStory.objects.filter(user=request.user, story=user_story,follow=True).exists()
    if request.user.is_authenticated:
        cont = UserStory.objects.filter(user=request.user, story=user_story,read=True)
        return render(request, 'app/story.html', {"authors": myAuthors, 'chapters': myChapter, 'story': myStory, 'category': myCategory, 'is_following': is_following, "continue":cont})
    
    return render(request, 'app/story.html', {"authors": myAuthors, 'chapters': myChapter, 'story': myStory, 'category': myCategory, 'is_following': is_following})
    
def chapter(request, story_id, chapter_id):
    myStory = story.objects.filter(id=story_id)
    myChapter = chapters.objects.raw("select * from app_chapters where story_id = %s order by name",[story_id])
    myStory = story.objects.filter(id=story_id)
    myChapter = chapters.objects.raw("select * from app_chapters where story_id = %s order by name",[story_id])
    chapter = chapters.objects.raw("select * from app_chapters where story_id = %s and id = %s",[story_id, chapter_id])
    chaptertruoc= chapters.objects.raw("select * from app_chapters where story_id = %s and name < %s order by name desc limit 1",[story_id, chapter[0].name])
    chaptersau = chapters.objects.raw("select * from app_chapters where story_id = %s and name > %s order by name asc limit 1",[story_id, chapter[0].name])
    if request.user.is_authenticated:
        if UserStory.objects.filter(user=request.user,story=get_object_or_404(story, id=story_id),chapter=get_object_or_404(chapters, id=chapter_id),follow=True).exists():
            UserStory.objects.filter(user=request.user,story=get_object_or_404(story, id=story_id),read=True).delete()
            UserStory.objects.filter(user=request.user,story=get_object_or_404(story, id=story_id),chapter=get_object_or_404(chapters, id=chapter_id)).update(read=True,
                                 date=timezone.now())
        else:
            user_story = UserStory.objects.filter(user=request.user,story=get_object_or_404(story, id=story_id),read=True)
            if user_story.exists():
                user_story.update(chapter=get_object_or_404(chapters, id=chapter_id),date=timezone.now())
            else:
                UserStory.objects.create(user=request.user,story=get_object_or_404(story, id=story_id),read=True,chapter=get_object_or_404(chapters, id=chapter_id),date=timezone.now())
    
    if request.method == "POST":
        comment_content = request.POST.get('comment')
        reply_content = request.POST.get('reply')
        if 'delete' in request.POST:
            get_object_or_404(comment, id=int(request.POST.get('delete'))).delete()
        if comment_content and comment_content.strip() != '':
            addComment = comment.objects.create(content=comment_content,user=request.user,chapters_id=chapter_id)
            addComment.save()
        if reply_content and reply_content.strip() != '':
            parent_comment = get_object_or_404(comment, id=int(request.POST.get('hidden')))
            addReply = comment.objects.create(content=reply_content,user=request.user,chapters_id=chapter_id,parent= parent_comment)
            addReply.save()
        return redirect("/story/" + str(story_id) + "/chapter/" + str(chapter_id))
             
             
    myComment = comment.objects.filter(chapters=chapter_id)
        
    # Assuming 'file_path' is the path to your PDF file
    file_path = chapter[0].file.path

    # Check if the file is a PDF
    if file_path.endswith('.pdf'):
    # Open the PDF file in binary mode
     with open(file_path, 'rb') as pdf_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Get the number of pages in the PDF
        num_pages = len(pdf_reader.pages)

        # Initialize an empty string to store the content
        pdf_content = ""

        # Iterate through all pages and extract text
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            pdf_content += page.extract_text()

    # Now 'pdf_content' contains the text content of the PDF
     return render(request, 'app/chapter.html', {'chapter': chapter, 'chaptertruoc': chaptertruoc, 'chaptersau': chaptersau, 
                                                'story': myStory, 'list_chapter': myChapter, 'data': pdf_content, 'list_comment': myComment,
                                                })
    else:
    # If the file is not a PDF, proceed with your existing code for other file types
     with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    return render(request, 'app/chapter.html', {'chapter': chapter, 'chaptertruoc': chaptertruoc, 'chaptersau': chaptersau, 
                                                'story': myStory, 'list_chapter': myChapter, 'data': file_content, 'list_comment': myComment,
                                                })
    
def list_story_author(request, id):
    myAuthor = category.objects.raw("select * from app_author where id = %s",[id])
    myStory = story.objects.raw("select app_story.* from app_author join app_story_authors "
                               + "on app_author.id = author_id join app_story "
                               + "on app_story.id = story_id where app_author.id = %s",[id])
    return render(request, 'app/author.html', {'story':myStory, 'author':myAuthor,})

def history(request):
    if request.user.is_authenticated:
        read = UserStory.objects.filter(user=request.user,read=True)
        if request.method == "POST":
            story_delete = get_object_or_404(story, id=int(request.POST.get('delete')))
            delete = UserStory.objects.filter(user=request.user, read=True, story=story_delete)
            for user_story in delete:
                if user_story.follow == True:
                    UserStory.objects.create(user=request.user, follow=True, story=story_delete).save()
                    user_story.delete()
                else:
                    user_story.delete()
            return redirect("/history/")
        return render(request, 'app/history.html', {'read':read})
    
def danhsach(request,name):
    myStory = story.objects.filter(status=name)
    return render(request,"app/danhsach.html",{'story': myStory,})
