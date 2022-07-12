from pyexpat import model
from unittest.util import _MAX_LENGTH
from  .models import  Video
from django import forms

class Video_form(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title','youtube_url','youtube_id' ]
        labels = {'title': 'Title'}


class Search_form(forms.Form):
    search_item = forms.CharField(max_length=255, label="search for videos")
