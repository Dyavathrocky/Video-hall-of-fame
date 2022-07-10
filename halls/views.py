from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  authenticate , login
from .models import Hall , Video


# Create your views here.

def hi(request):
    return render(request, 'halls/home.html')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        view = super(SignUp, self).form_valid(form)
        username  = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view

#to create hall using class based views 

class Create_view(generic.CreateView):
    model = Hall
    template_name = "halls/create.html"
    fields = ['title']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(Create_view, self).form_valid(form)
        return redirect('home')


    
