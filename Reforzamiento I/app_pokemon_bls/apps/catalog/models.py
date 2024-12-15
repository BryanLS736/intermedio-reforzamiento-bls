from django.db import models

# Create your models here.

class Catalogo(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.TextField()
