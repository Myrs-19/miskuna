from django.db import models
from django.urls import reverse
# Create your models here.

class Panel(models.Model):
    title = models.CharField(max_length=100)
    
    def get_absolute_url(self):
        return reverse("add")

class Task(models.Model):
    text = models.TextField()
    panel = models.ForeignKey(Panel, on_delete=models.CASCADE)