from django.shortcuts import render
from .models import Product

def all_products(request):
    products = Product.objects.all()
    args = {'products': products}
    return render(request, 'products.html', args)