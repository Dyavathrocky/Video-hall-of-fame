from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import  reverse_lazy
from django.template import  RequestContext

from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  authenticate , login
from .models import Hall , Video
from .forms import Video_form , Search_form


# Create your views here.

def hi(request):
    return render(request, 'halls/home.html')

def dashboard(request):
    return render(request, 'halls/dashboard.html')


def add_video(request, pk):
    form = Video_form()
    serch_form = Search_form()
    
    
    if request.method == "POST":
        filed_form = Video_form(request.POST)
        if filed_form.is_valid():
            video = Video()
            video.title = filed_form.cleaned_data.get('title')
            video.youtube_id = filed_form.cleaned_data.get('youtube_id')
            video.youtube_url = filed_form.cleaned_data.get('youtube_url')
            video.hall = Hall.objects.get(pk=pk)
            video.save()
    return render(request , 'halls/addvideo.html', {'form':form , 'search1' : serch_form})

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
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(Create_view, self).form_valid(form)
        return redirect('home')

    
class Detail_view(generic.DetailView):
    model = Hall
    template_name = "halls/detail.html"
    context_object_name = "ra"
    
class Update_view(generic.UpdateView):
    model = Hall
    template_name = 'halls/update.html'
    context_object_name = 'up'
    fields = ['title']
    success_url = reverse_lazy('dashboard')


class Delte_View(generic.DeleteView):
    model = Hall
    context_object_name = 'dele'
    template_name = 'halls/delete.html'
    success_url = reverse_lazy('dashboard')
    
