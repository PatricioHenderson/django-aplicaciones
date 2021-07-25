from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def endpoint(a):
    print("Hola!")

    return HttpResponse('9/12/2018')
