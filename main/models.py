from random import choices

from django.db import models


class Yonalish(models.Model):
    nom = models.CharField(max_length=50)
    aktiv = models.CharField(max_length=50)


class Fan(models.Model):
    nom = models.CharField(max_length=40)
    assosiy = models.BooleanField()
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE)


class Ustoz(models.Model):
    ism = models.CharField(max_length=20)
    yosh = models.IntegerField()
    jins = models.CharField(max_length=25, choices=(('Erkak', 'Erkak'), ('Ayol', 'Ayol')))
    daraja = models.CharField(max_length=25, choices=(('Bakalavr', 'Bakalavr'), ('Magistr', 'Magistr')))
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE)
