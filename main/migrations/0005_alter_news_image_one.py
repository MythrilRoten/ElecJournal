<<<<<<< HEAD
# Generated by Django 4.0.4 on 2022-04-26 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_news_image_four_news_image_one_news_image_three_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image_one',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Представляемая картинка'),
        ),
    ]
=======
# Generated by Django 4.0.4 on 2022-04-26 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_news_image_four_news_image_one_news_image_three_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image_one',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Представляемая картинка'),
        ),
    ]
>>>>>>> f7b792b8f3c70d32510a18fe2815b5f7a34bcce9
