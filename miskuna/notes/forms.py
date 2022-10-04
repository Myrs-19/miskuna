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
        widget=forms.TextInput()
    )
    email = forms.EmailField(
        label='Почта',
        widget=forms.EmailInput()
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='имя пользователя',
        widget=forms.TextInput(),
        )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(),
    )