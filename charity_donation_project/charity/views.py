from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from .models import Donation, Institution, Category
from .forms import AddDonationForm


class LandingPageView(View):

    def get(self, request):
        donated_institutions = Donation.objects.all()
        list_of_donated_institutions = []
        for donation in donated_institutions:
            list_of_donated_institutions.append(donation.institution)
        number_of_institutions = len(set(list_of_donated_institutions))

        foundations = Institution.objects.get_queryset().filter(type='FND').order_by('id')

        paginator = Paginator(foundations, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        ctx = {
            'bag_quantity': Donation.get_quantity(),
            'donated_institutions': number_of_institutions,
            'foundations': foundations,
            'ngos': Institution.objects.filter(type='NGO'),
            'locals': Institution.objects.filter(type='LOC'),
            'page_obj': page_obj,
        }

        return render(request, 'charity/index.html', ctx)


# class FoundationsListView(ListView):
#     model = Institution
#     template_name = 'charity/index.html'
#     context_object_name = 'foundations'
#     paginate_by = 3
#     queryset = Institution.objects.filter(type='FND')


class AddDonationView(LoginRequiredMixin, View):

    def get(self, request):
        ctx = {
            'categories': Category.objects.all(),

        }
        return render(request, 'charity/form.html', ctx)

    def post(self, request):
        form = AddDonationForm(request.POST)
        print(request.POST)

        if form.is_valid():
            form.cleaned_data['categories']
            print(form.cleaned_data)
        print(form.errors)

        return render(request, 'charity/form-confirmation.html')


