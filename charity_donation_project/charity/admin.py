from django.contrib import admin

from .models import Category, Institution, Donation


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    ...


@admin.register(Institution)
class InstitutionModelAdmin(admin.ModelAdmin):
    ...

@admin.register(Donation)
class DonationModelAdmin(admin.ModelAdmin):
    ...
