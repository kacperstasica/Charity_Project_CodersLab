from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .forms import UserRegisterForm


class RegisterView(CreateView):
    model = get_user_model()
    form_class = UserRegisterForm
    success_url = reverse_lazy(
        'login'
    )
    template_name = 'users/register.html'
    # success_message = "%(username)s was created successfully. You are now able to log in!"

# class LoginView(View):
#     def get(self, request):
#         return render(request, 'users/login.html')

