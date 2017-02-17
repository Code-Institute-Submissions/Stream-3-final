from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django.core.exceptions import ValidationError
from simplemathcaptcha.fields import MathCaptchaField

class UserRegistrationForm(UserCreationForm):

    MONTH_ABBREVIATIONS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',
        'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
    MONTH_CHOICES = [(u'', u'Select Expiry Month')]
    MONTH_CHOICES.extend(list(enumerate(MONTH_ABBREVIATIONS, 1)))
    YEAR_CHOICES = [(u'', u'Select Expiry Year')]
    YEAR_CHOICES.extend([(i, i) for i in xrange(2017, 2040)])
    email = forms.EmailField(label='Your Email Address (Must Be A Valid Email Address)', required='required')
    credit_card_number = forms.CharField(label='Credit OR Debit Card Number', required='required')
    cvv = forms.IntegerField(label='Card Security Code (A 3 Digit Code On The Back Of Your Card)', max_value=999, required='required')
    expiry_month = forms.ChoiceField(label='Credit OR Debit Card Expiry Month', choices=MONTH_CHOICES, required='required' )
    expiry_year = forms.ChoiceField(label='Credit OR Debit Card Expiry Month', choices=YEAR_CHOICES, required='required')
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    password1 = forms.CharField(label='Please Select a Password (Minimum 8 Characters Long and a Mixture of Letters and Numbers)', widget=forms.PasswordInput(), required='required')
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput(), required='required')
    captcha = MathCaptchaField(label='Please Answer This Math Problem to Prove Your Are Human', required=True)
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise ValidationError("Password must be at least 8 chars.")
        #check for number
        if not any(char.isdigit() for char in password1):
            raise ValidationError('Password must contain at least 1 digit.')

        # check for letter
        if not any(char.isalpha() for char in password1):
            raise ValidationError('Password must contain at least 1 letter.')
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password2')
        if len(password1) < 8:
            raise ValidationError("Password must be at least 8 chars.")
            if not any(char.isdigit() for char in password2):
                raise ValidationError('Password must contain at least 1 digit.')

            if not any(char.isalpha() for char in password2):
                raise ValidationError('Password must contain at least 1 letter.')
            return password1
        return password1

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'stripe_id']
        exclude = ['username']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password1')

        if password1 and password2 and password1 != password2:
            message = "Passwords do not match"
            raise ValidationError(message)
        return password2

    def save(self, commit=True):
        instance = super(UserRegistrationForm, self).save(commit=False)
        instance.username = instance.email
        if commit:
            instance.save()
        return instance

class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserResetForm(forms.Form):
    username = forms.CharField(label="User Email", widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    hashemail = forms.CharField(widget=forms.HiddenInput())

class ResetPasswordForm(forms.ModelForm):

    username = forms.CharField(label="User Email", widget=forms.TextInput(attrs={'readonly':'readonly'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password1 != password2:
            raise forms.ValidationError("Your passwords do not match")
        return password2

    def save(self, commit=True):
        instance = super(ResetPasswordForm, self).save(commit=False)
        instance.set_password(self.cleaned_data["password2"])
        instance.is_active = True
        if commit:
            instance.save()

        return instance