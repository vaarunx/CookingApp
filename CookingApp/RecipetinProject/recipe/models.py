from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


cuisineChoices = (
    ("Indian" , "Indian"),
    ("Chinese" , "Chinese"),
    ("Italian" , "Italian"),
    ("American" , "American"),
    ("Other" , "Other")
)

# Create your models here.
class Recipe(models.Model): 
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    ingredients = models.TextField(null= True)
    steps = models.TextField(null= True)
    datePosted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to = 'food_pics' , null = True)
    author = models.ForeignKey(User , on_delete= models.CASCADE)


    def __str__(self):
        return self.name + " " + self.cuisine   

    def get_absolute_url(self):
        return reverse('recipe-detail' , kwargs = {'pk' : self.pk})        
    
