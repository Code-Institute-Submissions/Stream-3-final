from django.test import TestCase
from .models import User
from forms import UserRegistrationForm, UserResetForm
from django import forms
from django.conf import settings


class TesUserSetup(TestCase):
    def test_user_reg(self):
        form = UserRegistrationForm({
            'email': 'test101@jatest.com',
            'password1': 'test1234',
            'password2': 'test1234',
            'stripd_id': settings.STRIPE_SECRET,
            'credit_card_number': '4242424242424242',
            'cvv': '123,',
            'expiry_month': '12',
            'expiry_year': '2018'
        })

        #self.assertTrue(form.is_valid())
        self.assertFalse(form.is_valid())


