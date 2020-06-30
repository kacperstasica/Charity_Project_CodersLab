from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, FormView


class LandingPageView(TemplateView):
    template_name = 'charity/index.html'


class AddDonationView(FormView):
    template_name = 'charity/form.html'


