from django.conf import settings
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver

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
    
@receiver(pre_delete, sender=story)
def remove_file(**kwargs):
    instance = kwargs.get('instance')
    instance.file.delete(save=False)
    
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
    
class comment(models.Model):
    comments = models.CharField(default='', max_length=255,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    chapters = models.ForeignKey(chapters,blank=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.comments} {self.date}"
