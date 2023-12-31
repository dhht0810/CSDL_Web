from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import CustomUser
# Register your models here.  
class CustomUserAdmin(UserAdmin):
    model = CustomUser  
  
    list_display = ('username', 'is_staff', 'is_active',)  
    list_filter = ('username', 'is_staff', 'is_active',)
    fieldsets = (  
        (None, {'fields': ('username', 'password')}),  
        ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser','user_permissions',)}),  
    )  
    add_fieldsets = (  
        (None, {  
            'classes': ('wide',),  
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active','is_superuser','user_permissions',)}  
        ),  
    )  
    search_fields = ('username',)  
    ordering = ('username',)  
    filter_horizontal = ('user_permissions',)  
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(username=request.user.username) 

admin.site.register(CustomUser, CustomUserAdmin)