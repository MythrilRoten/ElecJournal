from django import views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.func__auth),
    path('main', views.func__main_content)
]
