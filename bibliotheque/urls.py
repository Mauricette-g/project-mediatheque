

from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('home', home, name='home'),
    path('membres', home, name='membres'),
    path('livres', livres, name='livres'),
    path('dvds', dvds, name='dvds'),
    path('cds', cds, name='cds'),
    path('jeux', jeux, name='jeux'),
    path('ajouter-membre', AjoutMembre.as_view(), name="ajouter-membre"),
    path('update-membre/<int:pk>/', UpdateMembre.as_view(), name="update-membre"),
    path('delete-membre/<int:pk>/', DeleteMembre.as_view(), name="delete-membre"),
    path('ajouter-livre', AjoutLivre.as_view(), name="ajouter-livre"),
    path('update-livre/<int:pk>/', UpdateLivre.as_view(), name="update-livre"),
    path('delete-livre/<int:pk>/', DeleteLivre.as_view(), name="delete-livre"),
    path('ajouter-dvd', AjoutDVD.as_view(), name="ajouter-dvd"),
    path('update-dvd/<int:pk>/', UpdateDVD.as_view(), name="update-dvd"),
    path('delete-dvd/<int:pk>/', DeleteDVD.as_view(), name="delete-dvd"),
    path('ajouter-cd', AjoutCD.as_view(), name="ajouter-cd"),
    path('update-cd/<int:pk>/', UpdateCD.as_view(), name="update-cd"),
    path('delete-cd/<int:pk>/', DeleteCD.as_view(), name="delete-cd"),
    path('ajouter-jeu', AjoutJeu.as_view(), name="ajouter-jeu"),
    path('update-jeu/<int:pk>/', UpdateJeu.as_view(), name="update-jeu"),
    path('delete-jeu/<int:pk>/', DeleteJeu.as_view(), name="delete-jeu"),
]

