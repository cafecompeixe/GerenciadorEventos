from rest_framework.serializers import ModelSerializer
from core.models import Evento, Sobre

class EventoSerializer(ModelSerializer):
    class Meta:
        model = Evento
        fields = ('id', 'nome', 'descricao', 'data', 'hora_evento', 'atividade', 'endereco')

class SobreSerializer(ModelSerializer):
    class Meta:
        model = Sobre
        fields = ('__all__')
