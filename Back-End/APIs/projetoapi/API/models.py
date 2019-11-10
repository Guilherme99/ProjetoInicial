from django.db import models
from django.contrib.auth.models import User
    
class Usuario(models.Model):

  nome = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )
  usuario = models.CharField(
    max_length=255,
    null=False,
    blank=False,
    unique=True
  )
  senha = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )

  email = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )

  objetos = models.Manager()

  
class Registros(models.Model):

  ferramenta_registrada = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )
  id_usuario = models.IntegerField(
    null=False,
    blank=False
  )

  objects = models.Manager()
