<<<<<<< HEAD
# Generated by Django 4.0.4 on 2022-04-26 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_news_image_four_alter_news_image_one_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image_four',
            field=models.ImageField(blank=True, upload_to='photos/<built-in function id><django.db.models.fields.CharField>/fourth.jpg', verbose_name='Картинка №4'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image_one',
            field=models.ImageField(blank=True, upload_to='photos/<built-in function id><django.db.models.fields.CharField>/main.jpg', verbose_name='Представляемая картинка'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image_three',
            field=models.ImageField(blank=True, upload_to='photos/<built-in function id><django.db.models.fields.CharField>/third.jpg', verbose_name='Картинка №3'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image_two',
            field=models.ImageField(blank=True, upload_to='photos/<built-in function id><django.db.models.fields.CharField>/second.jpg', verbose_name='Картинка №2'),
        ),
    ]
=======
# Generated by Django 4.0.4 on 2022-04-26 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_news_image_four_alter_news_image_one_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image_four',
            field=models.ImageField(blank=True, upload_to='photos/<built-in function id><django.db.models.fields.CharField>/fourth.jpg', verbose_name='Картинка №4'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image_one',
            field=models.ImageField(blank=True, upload_to='photos/<built-in function id><django.db.models.fields.CharField>/main.jpg', verbose_name='Представляемая картинка'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image_three',
            field=models.ImageField(blank=True, upload_to='photos/<built-in function id><django.db.models.fields.CharField>/third.jpg', verbose_name='Картинка №3'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image_two',
            field=models.ImageField(blank=True, upload_to='photos/<built-in function id><django.db.models.fields.CharField>/second.jpg', verbose_name='Картинка №2'),
        ),
    ]
>>>>>>> f7b792b8f3c70d32510a18fe2815b5f7a34bcce9
