from django import forms

from .models import Donation


class AddDonationForm(forms.ModelForm):

    class Meta:
        model = Donation
        exclude = ('user', )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(AddDonationForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.user = self.user
        return super().save(commit)
