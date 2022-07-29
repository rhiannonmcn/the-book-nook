# Generated by Django 4.0.6 on 2022-07-29 11:46

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('book_author', models.CharField(max_length=200)),
                ('book_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('book_blurb', models.TextField()),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('book_approved', models.BooleanField(default=False)),
                ('book_created_on', models.DateTimeField(auto_now_add=True)),
                ('book_favourites', models.ManyToManyField(blank=True, related_name='book_favourites', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-book_created_on'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_detail', models.TextField()),
                ('review_created_on', models.DateTimeField(auto_now_add=True)),
                ('review_approved', models.BooleanField(default=False)),
                ('book_listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='book.book')),
                ('review_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-review_created_on'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='book_genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='book_genre', to='book.genre'),
        ),
        migrations.AddConstraint(
            model_name='book',
            constraint=models.UniqueConstraint(fields=('title', 'book_author'), name='unique_book_listing_ci'),
        ),
    ]
