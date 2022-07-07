from django import views
from django.urls import path
from django.contrib.auth import admin
from django.contrib.auth.views import LoginView , LogoutView
from  .views import hi , Create_view


from halls import views

urlpatterns = [
    path('', hi, name='home'),
    path('signup', views.SignUp.as_view(), name='signup'),
    path('login',LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('createhall/', Create_view.as_view(), name='createhall'),
]
