from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm, AuthenticationForm
from django.contrib.auth.forms import UserChangeForm
from django import forms
from django.contrib.auth.hashers import check_password
from django.utils import timezone

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
    """
    this is form for admin page to change CustomUser
    """
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', )


class UserChangeNameForm(forms.ModelForm):
    """
    this is form for user to change his data on the app
    """

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', )


class ConfirmPasswordForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ('confirm_password', )

    def clean(self):
        cleaned_data = super(ConfirmPasswordForm, self).clean()
        confirm_password = cleaned_data.get('confirm_password')
        if not check_password(confirm_password, self.instance.password):
            self.add_error('confirm_password', 'Hasło nie pasuje.')

    def save(self, commit=True):
        user = super(ConfirmPasswordForm, self).save(commit)
        user.last_login = timezone.now()
        if commit:
            user.save()
        return user


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

