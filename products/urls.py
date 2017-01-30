from django.conf.urls import url, include
from products import views as product_views

urlpatterns = [
    url(r'^products/$', product_views.all_products)
]