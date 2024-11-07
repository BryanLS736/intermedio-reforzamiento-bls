from django.db import models

# Create your models here.

class Pokemones(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=25)
    numero = models.IntegerField(default=0)
