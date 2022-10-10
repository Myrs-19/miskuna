from email.policy import default
from django.db import models
from django.urls import reverse

#мои импорты django
from django.contrib.auth.models import User


class Panel(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1) #pk=1 - запись админа admin_Mike 


class Task(models.Model):
    text = models.TextField()
    panel = models.ForeignKey(Panel, on_delete=models.CASCADE)