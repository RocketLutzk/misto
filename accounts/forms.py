from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
)

from .models import *

User = get_user_model()


class MyUserLoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control mt-5',
            'autofocus': '',
            'style': 'width:66ch',
            'placeholder': 'Імя користувача...',
        }
    ), )

    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Пароль...',
        }
    ), )

    # https://docs.djangoproject.com/en/2.1/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError(
                    'Користувача не знайдено,для початку зареєструйтесь')
            elif not user.check_password(password):
                raise forms.ValidationError(
                    'Пароль не правилний!')
            elif not user.is_active:
                raise forms.ValidationError(
                    'Користувач не активований')


class MyUserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control mt-5',
            'autofocus': '',
            'style': 'width:66ch',
            'placeholder': 'Імя користувача...',
        }
    ), )
    email1 = forms.EmailField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Електрона адреса',
        }
    ), )
    email2 = forms.EmailField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Підтвердіть електрону адресу',
        }
    ), )
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Введіть пароль...',
        }
    ), )

    class Meta:
        model = User
        fields = ['username', 'email1', 'email2', 'password', ]

    # https://docs.djangoproject.com/en/2.1/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other
    def clean(self):
        super().clean()
        email1 = self.cleaned_data.get('email1')
        email2 = self.cleaned_data.get('email2')
        if email1 != email2:
            raise forms.ValidationError('Email addresses must match!')
        email_qs = User.objects.filter(email=email1)
        if email_qs.exists():
            raise forms.ValidationError('Email address already registered!')


class CreateBox(forms.ModelForm):
    From = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control mt-2',
            'autofocus': '',
            'style': 'width:66ch',
            'placeholder': 'Звідки',
        }
    ))
    To = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control mt-2',
            'autofocus': '',
            'style': 'width:66ch',
            'placeholder': 'Куди',
        }
    ))
    name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control mt-2',
            'autofocus': '',
            'style': 'width:66ch',
            'placeholder': 'Імя',
        }
    ))
    lastName = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control mt-2',
            'autofocus': '',
            'style': 'width:66ch',
            'placeholder': 'Прізвище',
        }
    ))
    number = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control mt-2',
            'autofocus': '',
            'style': 'width:66ch',
            'placeholder': 'Номер телефону',
        }
    ))
    email = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control mt-2',
            'autofocus': '',
            'style': 'width:66ch',
            'placeholder': 'Електрона адреса',
        }
    ))
    description = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control ',
            'placeholder': 'Опис',
        }
    ))
    image = forms.FileField(label='Прикріпіть зображення посилки',)
    wiegth = forms.CharField(label='', widget=forms.TextInput(
        attrs={

            'class': 'form-control',
            'placeholder': 'Вага',
        }
    ))
    price = forms.DecimalField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control ',
            'placeholder': 'Ціна',
        }
    ))

    class Meta:
        model = Box
        exclude = ["slug","author"]
