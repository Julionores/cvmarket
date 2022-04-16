from datetime import date
from email.policy import default
from pyexpat import model
from tabnanny import verbose
#from tkinter import Place
from django.conf import settings
from django.db import models
from django.utils import timezone


class Cv(models.Model):
    MASCULIN = 'MASCULIN'
    FEMININ = 'FEMININ'
    
    SEXE_CHOICES = (
        (MASCULIN, 'Masculin'),
        (FEMININ, 'Feminin'),
    )

    class MatrimonialeType(models.TextChoices):
        CELIBATAIRE = 'Célibataire'
        MARIEE = 'Mariée'
        VEUVE = 'Veuve'
        DIVORCEE = 'Divorcée'

    nomcv = models.CharField(max_length=128, verbose_name="nom de votre cv")
    sexe = models.CharField(max_length=30, choices=SEXE_CHOICES)
    matrimoniale = models.CharField(max_length=50, choices=MatrimonialeType.choices, verbose_name="situation matrimoniale")
    enfant = models.BooleanField(default=False)
    telephone = models.CharField(max_length=128, verbose_name='numéro de téléphone')
    formation = models.TextField(max_length=256)
    competence = models.CharField(max_length=128, null=True, blank=True)
    experience_A = models.TextField(max_length = 256, blank=True, null=True, verbose_name="Experience Académique")
    experience_P = models.TextField(max_length = 256, blank=True, null=True, verbose_name="Experience Professionnelle")
    langue = models.CharField(max_length=128, default="anglais:faible;francais:moyen;chinois:parfait", verbose_name="langue parlée")
    certifications = models.TextField(blank=True, null=True, max_length=128)
    reference = models.CharField(max_length=128, null = True, blank=True)
    description = models.TextField(max_length=128, null=True, blank=True)
    usercv = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_edit = models.DateTimeField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.date_edit = timezone.now()
        super().save(*args, **kwargs)

class Lettre(models.Model):
    date = models.DateField()
    ville = models.CharField(max_length=128)
    destinateur = models.CharField(max_length=128)
    objet = models.CharField(max_length=128)
    profession = models.CharField(max_length=128)
    lettre = models.TextField(max_length=512, verbose_name="lettre de motivation")
    jointe = models.CharField(max_length=128, verbose_name="piece jointe")
    usercv = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_edit = models.DateTimeField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.date_edit = timezone.now()
        super().save(*args, **kwargs)

class Contact(models.Model):
    nomuser = models.CharField(max_length=128, default="Administrateur")
    message = models.TextField(max_length=512)
    usercv = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    deactive = models.BooleanField(default=True)
    date_edit = models.DateTimeField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.date_edit = timezone.now()
        super().save(*args, **kwargs)

