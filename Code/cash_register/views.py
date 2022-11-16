from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Product

def index(request):
    context = {'latest_question_list': 1}
    return render(request, 'cash_register/index.html', context)

def scan(request, code):
    product = Product.objects.get(code=code)
    context = {'product': product}
    return render(request, 'cash_register/scan.html', context)
