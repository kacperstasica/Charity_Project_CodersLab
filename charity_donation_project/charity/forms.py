from django import forms

from .models import Category


class AddDonationForm(forms.ModelForm):
    # categories = forms.MultipleChoiceField(
    #     choices=[('clothes-to-use', 1)]
    # )
    class Meta:
        model = Category
        fields = '__all__'
