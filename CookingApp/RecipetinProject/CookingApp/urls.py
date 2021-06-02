from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name = "CookingApp-home"),
    path('about/' , views.about , name = "CookingApp-about" ),
    path('main/' , views.main , name = "CookingApp-Main"),
]


