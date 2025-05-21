

from django.urls import path
from .views import *

urlpatterns = [
    path('', Accueil, name='accueil'),
]