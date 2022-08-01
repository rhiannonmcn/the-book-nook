# Generated by Django 4.0.6 on 2022-07-31 22:59

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_bookreview_book_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='genre_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
