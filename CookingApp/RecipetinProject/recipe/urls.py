from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipes , name = "recipe-home"),
    path('addRecipe/' , views.addRecipe ,name = "addRecipe")
]