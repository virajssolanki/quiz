from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import User


class UserRegisterForm(UserCreationForm):
    '''
    register user form
    '''
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'name']