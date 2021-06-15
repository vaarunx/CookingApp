from django.urls import path
from . import views
from .views import RecipeListView, RecipeCreateList, RecipeDetailView, RecipeUpdateList, RecipeDeleteList

urlpatterns = [
    path('user/<str:username>/', RecipeListView.as_view() , name = "recipe-home"),
    path('createRecipe/', RecipeCreateList.as_view() , name = "recipe-create"),
    path('<int:pk>/', RecipeDetailView.as_view() , name = "recipe-detail"),
    path('<int:pk>/update', RecipeUpdateList.as_view() , name = "recipe-update"),
    path('<int:pk>/delete', RecipeDeleteList.as_view() , name = "recipe-delete"),







]