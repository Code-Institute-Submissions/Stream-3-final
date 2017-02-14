from django import forms
from captcha.fields import CaptchaField

from .models import contact_data

class contactForm(forms.ModelForm):
    captcha = CaptchaField(label='Please repeat the characters below')
    name = forms.CharField(label='Your Name', required='required')
    email = forms.EmailField(label='Your Email Address So We Can Reply', min_length=5, required='required')
    phone = forms.CharField(label='Your Phone Number (Optional)', required=False)
    enquiry = forms.CharField(widget=forms.Textarea, label='Please Detail Your Enquiry Below:')
    class Meta:
        model = contact_data
        fields = ['name', 'email', 'phone', 'enquiry']