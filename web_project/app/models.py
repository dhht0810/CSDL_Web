from django.conf import settings
from django.db import models
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class author(models.Model):
    name = models.CharField(default="", max_length=50, blank=True)
    
    def __str__(self):
        return f"{self.name}"

class category(models.Model):
    name = models.CharField(default="", max_length=50)
    content = models.TextField(default="", max_length=1000)
    
    def __str__(self):
        return f"{self.name}"
    
class story(models.Model):
    CHOICES = (
        ("HT", "Hoàn thành"),
        ("DCN", "Đang cập nhật"),
    )
    image = models.ImageField(upload_to="app/image")
    name = models.CharField(default="", max_length=255)
    authors = models.ManyToManyField(author, blank=True)
    status = models.CharField(choices=CHOICES, max_length=255,default='')
    date =  models.DateField(auto_now_add=True)
    alias = models.CharField(default="", max_length=255)
    content = models.TextField(default="", max_length=1000)
    categories = models.ManyToManyField(category,blank=True)
    
    def __str__(self):
        return f"{self.name}"
    def get_absolute_url(self):
        return reverse('story', args=[int(self.id)])
    
#@receiver(pre_delete, sender=story)
#def remove_file(**kwargs):
 #   instance = kwargs.get('instance')
   # instance.file.delete(save=False)

   
class chapters(models.Model):
    name = models.CharField(default="", max_length= 50)
    date =  models.DateField(auto_now_add=True)
    file = models.FileField(upload_to="app/file")
    story = models.ForeignKey(story,blank=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} {self.file} {self.date}"
    
@receiver(pre_delete, sender=chapters)
def remove_file(**kwargs):
    instance = kwargs.get('instance')
    instance.file.delete(save=False)
    
    
class UserStory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    story = models.ForeignKey(story, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=chapters)
def send_update_notification(sender, instance, created, **kwargs):
    if created:
        user_stories = UserStory.objects.filter(story=instance.story)
        for user_story in user_stories:
            user_story.read = False
            user_story.save()
    
class comment(MPTTModel):
    content = models.CharField(default='', max_length=255,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    chapters = models.ForeignKey(chapters,blank=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.content} {self.date}"
    class MPTTMeta:
        order_insertion_by = ['content']
