from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, FormView, DetailView


from .models import Donation, Institution


class LandingPageView(TemplateView):
    model = Donation
    template_name = 'charity/index.html'

    def get_context_data(self, *args , **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['quantity'] = Donation.get_quantity()
        institutions = Donation.objects.all()
        list_of_donated_institutions = []
        for donation in institutions:
            list_of_donated_institutions.append(donation.institution)
        number_of_institutions = len(set(list_of_donated_institutions))
        context['institutions'] = number_of_institutions
        return context


class AddDonationView(FormView):
    template_name = 'charity/form.html'
