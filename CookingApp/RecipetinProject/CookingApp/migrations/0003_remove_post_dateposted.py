# Generated by Django 3.2 on 2021-05-31 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CookingApp', '0002_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='datePosted',
        ),
    ]
