from django.db import models

class Usuario(models.Model):

  nome = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )
  usuario = models.CharField(
    max_length=255,
    null=False,
    blank=False
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
