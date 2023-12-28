from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import AnnouncedPuResult


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class PollingForm(forms.ModelForm):
    class Meta:
        model = AnnouncedPuResult
        fields = ('state', 'lga', 'ward', 'polling_unit')
        # widgets = {
        #     'state': forms.Select(attrs={'class': 'form-control'}),
        #     'lga': forms.Select(attrs={'class': 'form-control'}),
        #     'ward': forms.Select(attrs={'class': 'form-control'}),
        #     'polling_unit': forms.Select(attrs={'class': 'form-control'}),
        # }
