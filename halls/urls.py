from ast import Delete
from django import views
from django.urls import path
from django.contrib.auth import admin
from django.contrib.auth.views import LoginView , LogoutView
from  .views import hi , Create_view , Detail_view , dashboard , Update_view , Delte_View ,add_video


from halls import views

urlpatterns = [
    path('', hi, name='home'),
    path('Dashboard/',dashboard , name='dashboard'),
    path('signup', views.SignUp.as_view(), name='signup'),
    path('login',LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('createhall/', Create_view.as_view(), name='createhall'),
    path('halloffame/<int:pk>/',Detail_view.as_view(), name="detailview" ),
    path('halloffame/<int:pk>/update', Update_view.as_view(), name='update' ),
    path('halloffame/<int:pk>/delete', Delte_View.as_view(), name = "delete"),
    path('halloffame/<int:pk>/addvideo', add_video , name='add_video' ),

    
]
