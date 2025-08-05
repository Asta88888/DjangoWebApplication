from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User


class UserRegisterForm(UserCreationForm):
    phone = forms.CharField(max_length=35, required=False)
    usable_password = None

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'phone')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('avatar', 'email', 'first_name', 'last_name', 'phone', 'country')

    def __init__(self, *args, **kwargs):
        """Инициализация формы и обновление атрибутов виджетов."""
        super().__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs.update({
            'class': 'form-control',
            'type': 'image'
        })
        self.fields['country'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите страну'
        })
        self.fields['phone'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите номер телефона'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите email'
        })
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите имя'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите фамилию'
        })
