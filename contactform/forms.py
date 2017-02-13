from django import forms
from captcha.fields import CaptchaField

from .models import contact_data

class contactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = contact_data
        fields = ['name', 'email', 'phone', 'enquiry']