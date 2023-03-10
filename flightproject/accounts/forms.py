from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm , UserChangeForm 
from .models import Customer

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ['username','email']

class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [ 'first_name','last_name','address','phone_number']