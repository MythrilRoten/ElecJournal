from tabnanny import verbose
from django.db import models
from django.forms import EmailField
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст новости')
    image_one = models.ImageField(upload_to=f'photos/%Y/%m/%d/main', blank=True, verbose_name='Представляемая картинка')
    image_two = models.ImageField(upload_to=f'photos/%Y/%m/%d/other', blank=True, verbose_name='Картинка №2')
    image_three = models.ImageField(upload_to=f'photos/%Y/%m/%d/other', blank=True, verbose_name='Картинка №3')
    image_four = models.ImageField(upload_to=f'photos/%Y/%m/%d/other', blank=True, verbose_name='Картинка №4')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    categ = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
    
    class Meta:
        verbose_name = 'Новости ТАТК ГА'
        verbose_name_plural = 'Новости ТАТК ГА'
        ordering = ['-time_create', 'title'] 


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})
    
    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['id']
