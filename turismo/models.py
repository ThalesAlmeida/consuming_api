from django.db import models

class Turismo(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=150)

