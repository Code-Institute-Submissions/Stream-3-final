import uuid
from django.db import models
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm

class Product(models.Model):

    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image1 = models.ImageField(blank=True, null=True)
    image2 = models.ImageField(blank=True, null=True)
    quantity_availabe = models.IntegerField(default=0)

    def paypal_form(self):
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": self.price,
            "currency": "GBP",
            "currency_code": "GBP",
            "item_name": self.name,
            "invoice": "%s-%s" % (self.pk, uuid.uuid4()),
            "notify_url": "%s/paypal-return" % settings.SITE_URL,
            "cancel_return": "%s/paypal_cancel" % settings.SITE_URL
        }
        return PayPalPaymentsForm(initial=paypal_dict)

    def __unicode__(self):
        return self.name