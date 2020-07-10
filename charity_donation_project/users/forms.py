from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm, AuthenticationForm
from django.contrib.auth.forms import UserChangeForm

from .models import CustomUser


class UserRegisterForm(DjangoUserCreationForm):

    class Meta(DjangoUserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Imie'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Nazwisko'
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail'
        self.fields['password1'].widget.attrs['placeholder'] = 'Hasło'
        self.fields['password2'].widget.attrs['placeholder'] = 'Potwierdzenie hasła'


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password')


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

