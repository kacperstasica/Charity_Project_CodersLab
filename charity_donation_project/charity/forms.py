from django import forms

from .models import Donation


class AddDonationForm(forms.ModelForm):

    class Meta:
        model = Donation
        fields = [
            'categories',
            'quantity',
            'institution',
            'address',
            'city',
            'zip_code',
            'pick_up_date',
            'pick_up_time',
            'pick_up_comment',
        ]
