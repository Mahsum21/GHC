from django.db import models
from django.db.models import deletion
from django.db.models.base import Model
from django.db.models.fields import DateField, DateTimeField
from django.db.models.fields.related import ForeignKey
from django.db.models.manager import ManagerDescriptor

# Create your models here.

class Personne(models.Model): 
    nom = models.CharField(max_length=255, null = False)
    prenom = models.CharField(max_length=255, null = False)
    fonction = models.CharField(max_length=255, null = False)
    statut = models.CharField(max_length=255, null = True)
    email = models.EmailField(max_length=255, null = False)
    mdp = models.CharField(max_length=255, null = False)
    photo = models.ImageField( null = True)
    # photo = models.URLField()
    dateEnregistrement = models.DateTimeField( auto_now_add=True)

class Formation(models.Model):
    nom = models.CharField(max_length=255, null=False, unique=True )
    lieu = models.CharField(max_length=255)
    responsable = models.ForeignKey(Personne, on_delete=models.CASCADE)
    personnes = models.ManyToManyField(Personne, related_name='formations', blank=True)

class Professeur(Personne):
    pass
    # professeur varchar(255) not null,
    # matiere varchar(255) not null

class Matiere(models.Model):
    nom = models.CharField(max_length=255, null=False)
    totalDuration = models.DurationField()
    currentDuration = models.DurationField()
    dailyDuration = models.DurationField()
    professeur = models.ManyToManyField(Professeur, related_name='matieres')


class Horaire(models.Model):
    joursDeCours = models.DateField()
    heureDeDebut = models.TimeField()
    specificite = models.CharField(max_length=255)
    aEuLieu = models.BooleanField(default=False)
    remarque = models.CharField(max_length=255) 
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    formations = models.ManyToManyField(Formation, related_name='horaires', blank=True)
