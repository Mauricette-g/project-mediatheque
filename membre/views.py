from django.shortcuts import render
from django.http import HttpResponse

from . models import *

# Create your views here.

def Accueil(request):
    return render(request, 'accueil.html', context={})

