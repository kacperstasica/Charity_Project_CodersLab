from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView, ListView

from .forms import UserRegisterForm, UserLoginForm, CustomUserChangeForm
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


class ProfileView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'users/profile.html'


class CustomUserUpdateView(LoginRequiredMixin, View):

    def get(self, request):
        form = CustomUserChangeForm(instance=request.user)
        context = {
            'form': form,
        }
        return render(request, 'users/edit_profile.html', context)

    def post(self, request):
        u_form = CustomUserChangeForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Twoje dane zostały zaktualizowane!')
            return redirect('users:profile')