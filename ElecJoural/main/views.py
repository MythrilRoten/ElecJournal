from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout


# Create your views here.

def func__auth(request):
    return render(request, 'main/auth.html')

def func__main_content(request):
    return render(request, 'main/main_content.html')
