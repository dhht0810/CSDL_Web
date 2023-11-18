from django.urls import path
from .views import *

urlpatterns = [
    path("signup/", register, name="register"),
    path("login/",login, name="login"),
    path("logout/",logout, name='logout'),
]