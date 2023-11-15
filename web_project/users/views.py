from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from app.models import comment

# Create your views here.

def register(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "users/register.html", {'form': form, })    

def login(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request,user)
            return redirect("/")
    return render(request, "users/login.html", {})
        
def logout(request):
    auth_logout(request)
    return redirect("/")
