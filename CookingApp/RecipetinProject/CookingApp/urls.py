from django.urls import path
from .views import PostViewList , DetailViewList , CreateViewList, UpdateViewList, DeleteViewList, UserPostViewList
from . import views

urlpatterns = [
    path('', PostViewList.as_view(), name = "CookingApp-home"),
    path('post/<int:pk>/', DetailViewList.as_view(), name = "post-detail"),
    path('post/<int:pk>/delete/', DeleteViewList.as_view(), name = "post-delete"),
    path('post/createPost/', CreateViewList.as_view(), name = "post-create"),
    path('post/<int:pk>/update/', UpdateViewList.as_view(), name = "post-update"),
    path('user/<str:username>', UserPostViewList.as_view(), name = "user-posts"),
    path('about/' , views.about , name = "CookingApp-about" ),
    path('main/' , views.main , name = "CookingApp-Main"),
]


