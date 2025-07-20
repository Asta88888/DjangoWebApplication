from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User


class UserRegisterForm(UserCreationForm):
    phone = forms.CharField(max_length=35, required=False)
    usable_password = None


    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'phone')
