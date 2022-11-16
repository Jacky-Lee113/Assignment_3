from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(request):
    context = {'latest_question_list': 1}
    return render(request, 'cash_register/index.html', context)
