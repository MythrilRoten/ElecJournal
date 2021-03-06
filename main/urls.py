from django.urls import path
from main.views import *


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='feedback'),
    path('login/', login, name='login'),
    path('grades/', table_grades, name='grades'),
    path('print/', printout, name='print'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category')
]