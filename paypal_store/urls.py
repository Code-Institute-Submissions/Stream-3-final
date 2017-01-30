from django.conf.urls import url, include
from paypal.standard.ipn import urls as paypal_urls
from paypal_store import views as paypal_views

urlpatterns = [
    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return', paypal_views.paypal_return),
    url(r'^paypal-cancel', paypal_views.paypal_cancel),
]