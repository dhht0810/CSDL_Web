from django.contrib import admin  
from django.contrib.auth import authenticate  
from django.contrib.auth.admin import UserAdmin  
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.  
class CustomUserAdmin(UserAdmin):  
    add_form = CustomUserCreationForm  
    form = CustomUserChangeForm  
    model = CustomUser  
  
    list_display = ('username', 'is_staff', 'is_active',)  
    list_filter = ('username', 'is_staff', 'is_active',)  
    fieldsets = (  
        (None, {'fields': ('username', 'password')}),  
        ('Permissions', {'fields': ('is_staff', 'is_active')}),  
    )  
    add_fieldsets = (  
        (None, {  
            'classes': ('wide',),  
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active')}  
        ),  
    )  
    search_fields = ('username',)  
    ordering = ('username',)  
    filter_horizontal = ()  
  
admin.site.register(CustomUser, CustomUserAdmin)  