from django.contrib.auth import views    
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from account.forms import UserRegisterForm


class Login(views.LoginView):
    '''
    login
    '''
    template_name = 'login.html'



class SignUpView(SuccessMessageMixin, generic.CreateView):
    '''
    create new user
    '''
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"