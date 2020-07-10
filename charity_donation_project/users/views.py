from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

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


class ProfileView(LoginRequiredMixin, TemplateView):
    model = CustomUser
    template_name = 'users/profile.html'


    # def get(self, request):
    #     user = self.request.user
    #     context = {
    #         'user': user
    #     }
    #     return render(request, 'users/profile.html', context)