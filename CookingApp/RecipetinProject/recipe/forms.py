from django import forms
from django.db.models import fields
from .models import Recipe

class RecipeEnteringForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name' , 'cuisine']