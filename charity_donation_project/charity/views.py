from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, TemplateView, FormView

from .models import Donation, Institution, Category
from .forms import AddDonationForm


class LandingPageView(View):

    def get(self, request):
        donated_institutions = Donation.objects.all()
        list_of_donated_institutions = []
        for donation in donated_institutions:
            list_of_donated_institutions.append(donation.institution)
        number_of_institutions = len(set(list_of_donated_institutions))

        # TODO: pagination
        # paginator = Paginator(foundations, 1)
        # page_number = request.GET.get('page')
        # page_obj = paginator.get_page(page_number)

        ctx = {
            'bag_quantity': Donation.get_quantity(),
            'donated_institutions': number_of_institutions,
            'foundations': Institution.objects.filter(type='FND'),
            'ngos': Institution.objects.filter(type='NGO'),
            'locals': Institution.objects.filter(type='LOC'),
            # 'page_obj': page_obj,
        }

        return render(request, 'charity/index.html', ctx)


class AddDonationView(LoginRequiredMixin, FormView):
    form_class = AddDonationForm
    success_url = reverse_lazy('confirmation')
    template_name = 'charity/form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        print(form.cleaned_data)
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.data)
        print('asdf')
        print(form.errors)
        return super().form_invalid(form)

    # def get(self, request, *args, **kwargs):
    #     ctx = {
    #         'categories': Category.objects.all(),
    #         'institutions': Institution.objects.all(),
    #     }
    #     return render(request, 'charity/form.html', ctx)


class ConfirmationView(LoginRequiredMixin, TemplateView):
    template_name = 'charity/form-confirmation.html'
