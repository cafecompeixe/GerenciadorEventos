from django.db import models

from atividade.models import Atividade
from endereco.models import Endereco
from presenca.models import Presenca


class Evento(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=150)
    data_evento = models.DateField()
    hora_evento = models.TimeField()
    atividade = models.ManyToManyField(Atividade)
    presenca = models.ManyToManyField(Presenca)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome
