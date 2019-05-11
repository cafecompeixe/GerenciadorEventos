from django.db import models


class Atividade(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    data_evento = models.DateField()
    hora = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
