# Generated by Django 4.0.6 on 2022-07-29 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_bookreview_book_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookreview',
            name='book_listing',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='book.book'),
            preserve_default=False,
        ),
    ]