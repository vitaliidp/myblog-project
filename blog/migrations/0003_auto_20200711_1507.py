# Generated by Django 3.0.6 on 2020-07-11 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200711_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='blog_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='blog_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='blog_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='blog_title',
            new_name='title',
        ),
    ]
