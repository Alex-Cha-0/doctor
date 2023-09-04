from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from app_doctor.models import Doctor, Orders, Route


class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'latitude', 'longitude']

        # widgets = {
        #     'name': forms.Select(attrs={
        #         'class': 'form-control',
        #     }),
        #     'latitude': forms.CharField(attrs={
        #         'class': 'form-control',
        #     }),
        #     'longitude': forms.CharField(attrs={'class': 'form-control'}),
        # }


class OrdersClientForm(ModelForm):
    class Meta:
        model = Orders
        fields = ['patient_name', 'text', 'latitude', 'longitude']


class OrdersUpdateForm(ModelForm):
    class Meta:
        model = Orders
        fields = ['doc_name', 'patient_name', 'text', 'is_active']


class RouteForm(ModelForm):
    class Meta:
        model = Route
        fields = ['doc_name', 'order', 'latitude', 'longitude']

class RouteFormUpdate(ModelForm):
    class Meta:
        model = Route
        fields = ['doc_name', 'order', 'latitude', 'longitude']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': "Username max 150"}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': "Пароль"}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': "Username max 150"}))
    email = forms.EmailField(label='E-mail',
                             widget=forms.EmailInput(attrs={"class": "form-control", 'placeholder': "email"}))
    first_name = forms.CharField(label='Имя',
                                 widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Имя"}))
    last_name = forms.CharField(label='Фамилия',
                                widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Фамилия"}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': "Пароль"}))
    password2 = forms.CharField(label='Повторить пароль', widget=forms.PasswordInput(
        attrs={"class": "form-control", 'placeholder': "Повторить пароль"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
