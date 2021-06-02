from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.


def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'CookingApp/home.html' , context)


def about(request):
    return render(request , 'CookingApp/about.html')


def main(request):
    return render(request, 'CookingApp/main.html')