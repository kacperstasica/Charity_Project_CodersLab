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
        foundations_list = Institution.objects.filter(type='FND').order_by('pk')
        paginator = Paginator(foundations_list, 4)
        page_number = request.GET.get('page')
        # print(page_number)  # to nie dziala, page_number jest None - why?
        # print(paginator.num_pages)
        fund_pages = paginator.get_page(page_number)

        ctx = {
            'bag_quantity': Donation.get_quantity(),
            'donated_institutions': number_of_institutions,
            'foundations': Institution.objects.filter(type='FND').order_by('pk'),
            'ngos': Institution.objects.filter(type='NGO'),
            'locals': Institution.objects.filter(type='LOC'),
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
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    # def get(self, request, *args, **kwargs):
    #     ctx = {
    #         'categories': Category.objects.all(),
    #         'institutions': Institution.objects.all(),
    #     }
    #     return render(request, 'charity/form.html', ctx)


class ConfirmationView(LoginRequiredMixin, TemplateView):
    template_name = 'charity/form-confirmation.html'
