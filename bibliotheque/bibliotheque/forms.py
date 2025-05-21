from django.forms import ModelForm
from .models import *

class MembreForm(ModelForm):
    class Meta:
        model=Membre
        fields='__all__'


class LivreForm(ModelForm):
    class Meta:
        model=Livre
        fields='__all__'

class DVDForm(ModelForm):
    class Meta:
        model=DVD
        fields='__all__'


class CDForm(ModelForm):
    class Meta:
        model=CD
        fields='__all__'


class JeuDePlateauForm(ModelForm):
    class Meta:
        model=JeuDePlateau
        fields='__all__'
