from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils import timezone


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    datePosted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User , on_delete= models.CASCADE)


    def __str__(self):
        return self.name + " " + self.cuisine   
    
