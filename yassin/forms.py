from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import TextInput, PasswordInput


class UserRegistrationForm(UserCreationForm):
    class Meta:

        model = User
        fields = ['username', 'email', 'password1','password2']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")

        return cleaned_data


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget= TextInput())
    password = forms.CharField(widget= PasswordInput())