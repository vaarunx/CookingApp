from django.contrib.auth import models
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

class PostViewList(ListView):
    model = Post
    template_name = "CookingApp/home.html"
    context_object_name = 'posts'
    ordering = ['-datePosted']

class UserPostViewList(ListView):
    model = Post
    template_name = "CookingApp/user_posts.html"
    context_object_name = 'posts'   

    def get_queryset(self):
        user = get_object_or_404(User , username= self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-datePosted')


class DetailViewList(DetailView):
    model = Post
    template_name = "CookingApp/postDetail.html"
    context_object_name = "post"


class CreateViewList(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "CookingApp/createPost.html"
    fields = ['title' , 'content']    
    success_url = "//localhost:8000"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateViewList(LoginRequiredMixin , UserPassesTestMixin , UpdateView):
    model = Post
    template_name = "CookingApp/createPost.html"
    fields = ['title' , 'content']    
    success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)        


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class DeleteViewList(LoginRequiredMixin , UserPassesTestMixin , DeleteView):
    model = Post
    template_name = "CookingApp/deletePost.html"
    context_object_name = "post"    
    success_url = "/"  


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'CookingApp/home.html' , context)




def about(request):
    return render(request , 'CookingApp/about.html')


def main(request):
    return render(request, 'CookingApp/main.html')