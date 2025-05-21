from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse


from .models import *
from .forms import *

# Create your views here.

def home(request):
    membres = Membre.objects.all()
    return render(request, "accueil.html", {'membres':membres})

### membres
class AjoutMembre(PermissionRequiredMixin,CreateView):
    model=Membre
    form_class=MembreForm
    template_name="ajouter_membre.html"
    success_url = reverse_lazy('membres')
    permission_required = 'bibliotheque.view_Membre'
 

class UpdateMembre(PermissionRequiredMixin,UpdateView):
    model=Membre
    form_class=MembreForm
    template_name="update_membre.html"
    success_url = 'membres'
    permission_required = 'bibliotheque.change_membre'


class DeleteMembre(PermissionRequiredMixin,DeleteView):
    model = Membre
    template_name="delete_membre.html"
    success_url = reverse_lazy("membres")
    permission_required = 'bibliotheque.delete_membre'



### livres

def livres(request):
    livres = Livre.objects.all()
    return render(request, "livres.html", {'livres':livres})

class AjoutLivre(PermissionRequiredMixin,CreateView):
    model=Livre
    form_class=LivreForm
    template_name="ajouter_livre.html"
    success_url = reverse_lazy('livres')
    permission_required = 'bibliotheque.view_Livre'
 
class UpdateLivre(PermissionRequiredMixin,UpdateView):
    model=Livre
    form_class=LivreForm
    template_name="update_livre.html"
    success_url = 'livres'
    permission_required = 'bibliotheque.change_livre'

class DeleteLivre(PermissionRequiredMixin,DeleteView):
    model = Livre
    template_name="delete_livre.html"
    success_url = reverse_lazy("livres")
    permission_required = 'bibliotheque.delete_livre'

### DVD
def dvds(request):
    dvds = DVD.objects.all()
    return render(request, "dvds.html", {'dvds':dvds})

class AjoutDVD(PermissionRequiredMixin,CreateView):
    model=DVD
    form_class=DVDForm
    template_name="ajouter_dvd.html"
    success_url = reverse_lazy('dvds')
    permission_required = 'bibliotheque.view_DVD'
 
class UpdateDVD(PermissionRequiredMixin,UpdateView):
    model=DVD
    form_class=DVDForm
    template_name="update_dvd.html"
    success_url = 'dvds'
    permission_required = 'bibliotheque.change_dvd'

class DeleteDVD(PermissionRequiredMixin,DeleteView):
    model = DVD
    template_name="delete_dvd.html"
    success_url = reverse_lazy("dvds")
    permission_required = 'bibliotheque.delete_dvd'

### CD
def cds(request):
    cds = CD.objects.all()
    return render(request, "cds.html", {'cds':cds})

class AjoutCD(PermissionRequiredMixin,CreateView):
    model=CD
    form_class=CDForm
    template_name="ajouter_cd.html"
    success_url = reverse_lazy('cds')
    permission_required = 'bibliotheque.view_CD'
 
class UpdateCD(PermissionRequiredMixin,UpdateView):
    model = CD
    form_class=CDForm
    template_name="update_cd.html"
    success_url = 'cds'
    permission_required = 'bibliotheque.change_cd'

class DeleteCD(PermissionRequiredMixin,DeleteView):
    model = CD
    template_name="delete_cd.html"
    success_url = reverse_lazy("cds")
    permission_required = 'bibliotheque.delete_cd'


### jeu
def jeux(request):
    jeux = JeuDePlateau.objects.all()
    return render(request, "jeux.html", {'jeux':jeux})

class AjoutJeu(PermissionRequiredMixin,CreateView):
    model = JeuDePlateau
    form_class=CDForm
    template_name="ajouter_jeu.html"
    success_url = reverse_lazy('jeux')
    permission_required = 'bibliotheque.view_JeuDePlateau'
 
class UpdateJeu(PermissionRequiredMixin,UpdateView):
    model = JeuDePlateau
    form_class=CDForm
    template_name="update_jeu.html"
    success_url = 'jeux'
    permission_required = 'bibliotheque.change_jeu'

class DeleteJeu(PermissionRequiredMixin,DeleteView):
    model = JeuDePlateau
    template_name="delete_jeu.html"
    success_url = reverse_lazy("jeux")
    permission_required = 'bibliotheque.delete_jeu'

