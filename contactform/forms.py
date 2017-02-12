from django import forms

from .models import contact_data

class contactForm(forms.ModelForm):
    class Meta:
        model = contact_data
        fields = ['name', 'email', 'phone', 'enquiry']