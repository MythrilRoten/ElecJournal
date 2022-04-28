<<<<<<< HEAD
from django.contrib import admin

from .models import *

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'image_one', 'image_two', 'image_three', 'image_four', 'is_published' )
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(News , NewsAdmin)
admin.site.register(Category, CategoryAdmin)
=======
from django.contrib import admin

from .models import *

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'image_one', 'image_two', 'image_three', 'image_four', 'is_published' )
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(News , NewsAdmin)
admin.site.register(Category, CategoryAdmin)
>>>>>>> f7b792b8f3c70d32510a18fe2815b5f7a34bcce9
