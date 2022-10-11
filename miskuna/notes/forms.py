from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *

class FormTask(forms.Form):
    text = forms.CharField(
        label='text',
        widget=forms.TextInput(),
        )


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={
            'id' : "forName",
            'type' : "text",
            'name' : "name",
            'class' : "form__input",
            'placeholder' : "Имя*:",
        })
    )
    
    email = forms.EmailField(
        label='Почта',
        widget=forms.EmailInput(attrs={
            'id' : "forEmail", 
            'type' : "text", 
            'name' : "Email", 
            'class' : "form__input", 
            'placeholder' : "E-mail*",
        })
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'id' : "userPassword",
            'type' : "password",
            'name' : "Пароль",
            'class' : "form__input",  
            'placeholder' : "Пароль",
        })
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput(attrs={
            'id' : "userPassword",
            'type' : "password",
            'name' : "Пароль",
            'class' : "form__input",  
            'placeholder' : "Пароль",
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    
    username = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={
            'id' : "forName",
            'type' : "text",
            'name' : "name",
            'class' : "form__input",
            'placeholder' : "Имя*:",
        }),
        )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'id' : "userPassword",
            'type' : "password",
            'name' : "Пароль",
            'class' : "form__input",  
            'placeholder' : "Пароль",
        }),
    )