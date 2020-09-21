from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
class Register(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
 

class Duty(forms.ModelForm):
    class Meta:
        model=Todo
        fields=["text","user"]
