from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Visitor


class Log_form(ModelForm):
    class Meta:
        model = Visitor
        fields = ['name']


class Login_form(forms.Form):
    user_name = forms.CharField(label='user_name', max_length=100)
    user_pwd = forms.CharField(label='user_password', max_length=100)


class Sign_up_form(forms.Form):
    first_name = forms.CharField(label='first name', max_length=100)
    last_name = forms.CharField(label='last name', max_length=100)
    email = forms.EmailField(label='email', max_length=100)
    user_name = forms.CharField(label='user_name', max_length=100)
    user_pwd = forms.CharField(label='user_password', max_length=100)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )