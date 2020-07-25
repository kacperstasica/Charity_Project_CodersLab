import datetime
from functools import wraps
from django.utils import timezone


def confirm_password(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        password = request.user.password
        print(password, '<--------------')
        if password is not None:
            from .views import ConfirmPasswordView
            return ConfirmPasswordView.as_view()(request, *args, **kwargs)
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def confirm_password_by_time_span(view_func):
    """
    if user was logged in for more than 6 hours, the view decorated with
    this decorator asks user for password confirmation
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        last_login = request.user.last_login
        time_span = last_login + datetime.timedelta(hours=6)
        if timezone.now() > time_span:
            from .views import ConfirmPasswordView
            return ConfirmPasswordView.as_view()(request, *args, **kwargs)
        return view_func(request, *args, **kwargs)
    return _wrapped_view