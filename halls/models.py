from django.db import models

# Create your models here.

class Hall(models.Model):
    title = models.CharField(max_length=255)

class Video(models.Model):
    title = models.CharField(max_length=255)
    youtube_url = models.CharField(max_length=255)
    desciption = models.TextField()
    url = models.URLField()
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
