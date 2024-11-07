from django.db import models

# Create your models here.

class Administrador(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField(default=0)
    pais = models.CharField(max_length=30)
    desactivado = models.BooleanField(default=False)
