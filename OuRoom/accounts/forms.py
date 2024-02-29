from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm
from django import forms
from .models import CustomUser, Profile



#Create/Register User - Model Form
class CreateUserForm(UserCreationForm):

    first_name = forms.CharField(max_length=15,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Imię',
                                                               'class': 'form-control',
                                                               'id': 'firstname',
                                                               }))
    last_name = forms.CharField(max_length=15,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Nazwisko',
                                                              'class': 'form-control',
                                                              'id': 'lastname',
                                                              }))
    username = forms.CharField(max_length=15,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Nazwa użytkownika',
                                                             'class': 'form-control',
                                                             'id': 'username',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           'id': 'email',
                                                           }))
    password1 = forms.CharField(max_length=15,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Hasło',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=15,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz hasło',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] # List of fields to be included in the form.

class UserUpdateForm(forms.ModelForm):

    last_name = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'}))

    first_name = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Imię'}))

    class Meta:
        model = CustomUser
        fields = ['last_name', 'first_name']

class SetPasswordForm(SetPasswordForm):

    new_password1 = forms.CharField(max_length=15, widget=forms.PasswordInput(attrs={'placeholder': 'Podaj nowe hasło'}))
    new_password2 = forms.CharField(max_length=15, widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz hasło'}))

    class Meta:
        model = CustomUser
        fields = ['new_password1', 'new_password2']

class ProfileUpdateForm(forms.ModelForm):

    location = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Lokalizacja'}))

    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'Data urodzenia'}))

    class Meta:
        model = Profile
        fields = ['location', 'birth_date']

#Authenticate a User - Model Form
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'username', 'placeholder': 'Login'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password', 'placeholder': 'Hasło'}))
