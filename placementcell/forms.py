from django import forms
from django.contrib.auth.models import User

class Recruiter_register_form(forms.ModelForm):
    organisation_name=forms.CharField()
    email = forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField(widget=forms.NumberInput)


    class Meta:
        model=User
        fields=['username','organisation_name','email','password','first_name','last_name','phone_number']

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
