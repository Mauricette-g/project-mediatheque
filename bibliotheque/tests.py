from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import *

class LivreTestCase(TestCase):
    def setUp(self):
        Livre.objects.create(name="Livre 1", auteur="Auteur 1")

    def test_livre_creation(self):
        livre = Livre.objects.get(name="Livre 1")
        self.assertEqual(livre.auteur, "Auteur 1")


#Testte la classe Emprunt
#class EmpruntTestCase(TestCase):
 #   def setUp(self):
  #      Emprunt.objects.create(livre="Livre 1", dvd="DVD 1", cd="CD 1", membre="Membre 1")

