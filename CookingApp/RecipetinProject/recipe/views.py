from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Recipe
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe/recipePage.html'
    context_object_name = "all_recipes"
    ordering = ['-datePosted']
    
    def get_queryset(self):
        user = get_object_or_404(User , username= self.kwargs.get('username'))
        return Recipe.objects.filter(author = user).order_by('-datePosted')

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe/recipeDetail.html"
    context_object_name = "recipe"


class RecipeCreateList(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "recipe/createRecipe.html"
    fields = ['name' , 'cuisine' , 'ingredients' , 'steps' ]    
    #success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateList(LoginRequiredMixin , UserPassesTestMixin , UpdateView):
    model = Recipe
    template_name = "recipe/createRecipe.html"
    fields = ['name' , 'cuisine' , 'ingredients' , 'steps' ]     
    success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)        


    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.author:
            return True
        return False


class RecipeDeleteList(LoginRequiredMixin , UserPassesTestMixin , DeleteView):
    model = Recipe
    template_name = "recipe/deleteRecipe.html"
    context_object_name = "recipe"    
    success_url = "/"


    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.author:
            return True
        return False










@login_required
def recipes(request):
    #form = RecipeEnteringForm()
    context = {

        'all_recipes': Recipe.objects.all(),
    }
    return render(request , "recipe/recipePage.html" , context)

@login_required
def addRecipe(request):
    if request.method == 'POST':
        new_item = Recipe(name = request.POST['DishName'] , cuisine = request.POST['Cuisine'] , ingredients = request.POST['Ingredients'] , steps = request.POST['Steps'])
        new_item.save()
    
    return HttpResponseRedirect('/recipe/')

@login_required
def deleteRecipe(request , recipe_id):
    if request.method == "POST":
        print(recipe_id)
        deleteItem = Recipe.objects.get(id = recipe_id)
        deleteItem.delete()
    
    return HttpResponseRedirect('/recipe/')




    