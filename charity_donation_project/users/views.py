from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView

from .decorators import confirm_password
from .forms import UserRegisterForm, UserLoginForm, UserChangeNameForm, ConfirmPasswordForm
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


# @method_decorator(confirm_password, name='dispatch')
class CustomUserUpdateView(LoginRequiredMixin, View):

    def get(self, request):
        form = UserChangeNameForm(instance=request.user)
        context = {
            'form': form,
        }
        return render(request, 'users/edit_profile.html', context)

    def post(self, request):
        u_form = UserChangeNameForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Twoje dane zostały zaktualizowane!')
            return redirect('profile')


class ConfirmPasswordView(UpdateView):
    form_class = ConfirmPasswordForm
    template_name = 'users/confirm_password.html'

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return self.request.get_full_path()
