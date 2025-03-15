from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Bonjour sur l'application de la bibliothèque.")

def detail(request, auteur):
    return HttpResponse("Voici le livre de %s." % auteur)


def results(request, auteur):
    response = "Voici le livre de l'auteur %s."
    return HttpResponse(response % auteur)


