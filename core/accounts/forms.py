from django.forms import ModelForm
import django_filters
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Property_images


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class Property_images(forms.ModelForm):
    class Meta:
        model = Property_images
        fields = ('prop_image_name', 'listing', 'image')
