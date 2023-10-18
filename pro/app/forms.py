from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs=({'class':'form-control', 'placeholder':'Enter Name'})))
    email_id = forms.CharField(widget=forms.TextInput(attrs=({'class':'form-control', 'placeholder':'Enter Mail id'})))
    phone_no = forms.CharField(widget=forms.TextInput(attrs=({'class':'form-control', 'placeholder':'Enter Phone Number'})))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=({'class':'form-control', "placeholder":"Enter password"})))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=({'class':'form-control', "placeholder":"Enter confirm password"})))

class Meta:
    models = User
    fields = ['username', 'email_id', 'phone_no', 'password1', 'password2']
