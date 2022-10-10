from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name='home'),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("login1/", user_login1, name="login1"),
    path("logout/", user_logout, name="logout"),
    
]