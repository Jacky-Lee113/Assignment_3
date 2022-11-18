from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Product, Cart

def index(request):
    context = {'products': Product.objects.all(),
               'title': 'Cash Register'}
    return render(request, 'cash_register/index.html', context)

def scan(request):
    code = request.GET['code']
    product = Product.objects.get(code=code)
    c = Cart(product=product, quantity=1)
    c.save()
    context = {'cart': Cart.objects.all(), 
               'total': Cart.total(),
               'products': Product.objects.all(),
               'title': 'Scan the code'
               }
    
    return render(request, 'cash_register/scan.html', context)

def checkout(request):
    context = {'cart': Cart.objects.all(),
               'title': 'Checkout'}
    Cart.objects.all().delete()
    return render(request, 'cash_register/checkout.html', context)
