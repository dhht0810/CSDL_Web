from django.db import models
from django.utils import timezone
from .managers import CustomUserManager 
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(default='',max_length=30,unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
 
    objects = CustomUserManager()
 
    def __str__(self):
        return f"{self.username}"
    
    def has_perm(self, perm, obj=None):  
        if self.is_active and self.is_superuser:
            return True
        return super().has_perm(perm, obj)