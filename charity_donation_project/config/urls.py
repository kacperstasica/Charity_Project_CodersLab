"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views


from charity import views as charity_view
from users import views as users_view


urlpatterns = [
    path('', charity_view.LandingPageView.as_view(), name='home'),
    path('login/', users_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', users_view.RegisterView.as_view(), name='register'),
    path('add_donation/', charity_view.AddDonationView.as_view(), name='add-donation'),
    path('profile/', users_view.ProfileView.as_view(), name='profile'),
    path('edit_profile/', users_view.CustomUserUpdateView.as_view(), name='edit-profile'),
    path('admin/', admin.site.urls),
]
