from django.contrib.auth.models import User
from django.db import models


class Presenca(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    presenca = models.BooleanField()

    def __str__(self):
        return self.usuario.username

