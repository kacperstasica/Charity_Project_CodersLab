from django.contrib.auth.views import LoginView as DjangoLoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserRegisterForm, UserLoginForm
from .models import CustomUser


class RegisterView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy(
        'login'
    )
    template_name = 'users/register.html'
    success_message = "%(email) was created successfully. You are now able to log in!"


class LoginView(DjangoLoginView):
    form_class = UserLoginForm

    def form_invalid(self, form):
        if form['username']:
            user_exists = CustomUser.objects.filter(email=form['username']).exists()
            if not user_exists:
                return redirect('register')

