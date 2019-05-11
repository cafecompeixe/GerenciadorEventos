from django.db import models


class Endereco(models.Model):
    nome_local = models.CharField(max_length=150)
    rua = models.CharField(max_length=150)
    bairro = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=150)

    def __str__(self):
        return self.nome_local
