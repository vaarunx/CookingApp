# Generated by Django 3.2 on 2021-06-10 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cuisine', models.CharField(max_length=100)),
                ('ingredients', models.TextField(null=True)),
                ('steps', models.TextField(null=True)),
                ('datePosted', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(null=True, upload_to='food_pics')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
