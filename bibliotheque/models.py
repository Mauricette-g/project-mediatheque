from django.db import models
# Create your models here.

# Classe pour les membres
class Membre(models.Model):
    name = models.CharField(max_length=255)
    bloque = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# Classe parente pour les médias
class Media(models.Model):
    nom = models.CharField(max_length=255)
    disponible = models.BooleanField(default=True)
    date_emprunt = models.DateField(null=True, blank=True)
    emprunteur = models.ForeignKey('Membre', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True

# Sous-classes héritant de Media
class Livre(Media):
    auteur = models.CharField(max_length=255)
    def __str__(self):
        return self.nom

class DVD(Media):
    realisateur = models.CharField(max_length=255)
    def __str__(self):
        return self.nom

class CD(Media):
    artiste = models.CharField(max_length=255)
    def __str__(self):
        return self.nom

# Classe pour les jeux de plateau
class JeuDePlateau(models.Model):
    name = models.CharField(max_length=255)
    createur = models.CharField(max_length=255)
    def __str__(self):
        return self.name

