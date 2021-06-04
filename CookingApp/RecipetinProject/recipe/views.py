from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import RecipeEnteringForm
from .models import Recipe
from django.http import HttpResponseRedirect , HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def recipes(request):
    #form = RecipeEnteringForm()
    context = {

        'all_recipes': Recipe.objects.all(),
    }
    return render(request , "recipe/recipePage.html" , context)

@login_required
def addRecipe(request):
    if request.method == 'POST':
        new_item = Recipe(name = request.POST['DishName'] , cuisine = request.POST['Cuisine'])
        new_item.save()
    
    return HttpResponseRedirect('/recipe/')

@login_required
def deleteRecipe(request , recipe_id):
    if request.method == "POST":
        print(recipe_id)
        deleteItem = Recipe.objects.get(id = recipe_id)
        deleteItem.delete()
    
    return HttpResponseRedirect('/recipe/')




    