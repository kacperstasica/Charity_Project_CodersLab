from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm, AuthenticationForm


class UserRegisterForm(DjangoUserCreationForm):

    class Meta(DjangoUserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Login'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Imie'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Nazwisko'
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail'
        self.fields['password1'].widget.attrs['placeholder'] = 'Hasło'
        self.fields['password2'].widget.attrs['placeholder'] = 'Potwierdzenie hasła'


class UserLoginForm(AuthenticationForm):

    class Meta:
        fields = [
            'username'
            'password'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'E-mail'
        self.fields['password'].widget.attrs['placeholder'] = 'Hasło'
