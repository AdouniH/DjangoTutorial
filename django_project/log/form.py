from django import forms

class Login_form(forms.Form):
    user_name = forms.CharField(label='user_name', max_length=100)
    user_pwd = forms.CharField(label='user_password', max_length=100)
