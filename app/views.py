from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dhoni(request):
    return HttpResponse('MSD is best finisher !!!!!!')
def rohit(request):
    return HttpResponse('this is the function of rohit belongs to app ')