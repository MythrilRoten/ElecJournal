from django.shortcuts import render

# Create your views here.

def func__auth(request):
    return render(request, 'main/auth.html')

def func__main_content(request):
    return render(request, 'main/main_content.html')