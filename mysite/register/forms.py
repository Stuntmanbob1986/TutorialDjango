from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        # class Meta ist nötig damit Eintraege in der DB geaendert/geschrieben werden koennen
        model = User
        fields = ["username", "email", "password1", "password2"]
        # email field wird zwischen username und password1/2 hinzugefuegt