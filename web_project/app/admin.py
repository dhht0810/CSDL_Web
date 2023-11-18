from django.contrib import admin
from .models import *

# Register your models here.
    
class ChaptersInline(admin.TabularInline):
    model = chapters
    
class StoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'list_of_authors',)
    
    search_fields = ['@name',]
    list_filter = ['name']
    date_hierarchy = 'date'
    inlines = [ChaptersInline]
    
    def list_of_authors(self, obj):
        return ("%s" % ','.join([author.name for author in obj.authors.all()]))
    list_of_authors.short_description = 'Authors'

admin.site.register(story, StoryAdmin)
admin.site.register(author)
admin.site.register(category)
admin.site.register(comment)