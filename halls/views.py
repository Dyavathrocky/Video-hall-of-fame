from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .models import Hall , Video


# Create your views here.

def hi(request):
    return render(request, 'halls/home.html')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'


#to create hall using class based views 

class Create_view(generic.CreateView):
    model = Hall
    template_name = "halls/create.html"
    fields = "__all__"
    success_url = reverse_lazy('home')


    
