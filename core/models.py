from django.db import models

from atividade.models import Atividade
from endereco.models import Endereco
from presenca.models import Presenca


class Evento(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=150)
    data = models.DateField()
    hora_evento = models.TimeField()
    atividade = models.ManyToManyField(Atividade)
    presenca = models.ManyToManyField(Presenca)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome

class Sobre(models.Model):
    programadores = models.CharField(max_length=250)
    gitHub = models.CharField(max_length=200)
    desricao = models.CharField(max_length=200)
    versaoDaAPI = models.CharField(max_length=20)
    versaoDoApp = models.CharField(max_length=20)
    dataDeCriacao = models.DateField()

    def __str__(self):
        return 'Sobre'
