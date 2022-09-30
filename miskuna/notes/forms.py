from django import forms

from .models import *

class FormTask(forms.Form):
    text = forms.CharField(
        label='text',
        widget=forms.TextInput(),
        )