from rest_framework.viewsets import ModelViewSet
from core.api.serializers import EventoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import Evento
from datetime import datetime  
from django.db.models import Q


class EventoViewSet(ModelViewSet):
    queryset = Evento.objects.all().order_by('-data')
    serializer_class = EventoSerializer

    @action(methods=['get'], detail=False)
    def ordenado(self, req):
        now = datetime.now()
        ordenado = self.get_queryset().filter(Q(data=now.date())|Q(data__gt=now.date())).order_by('-data')
        serializer = self.get_serializer_class()(ordenado, many=True)
        return Response(serializer.data)

    def get_eventos(self, data_ini, data_fim):
        data_ini = datetime.strptime(data_ini, "%Y-%m-%d").date()
        data_fim = datetime.strptime(data_fim, "%Y-%m-%d").date()
        return Evento.objects.order_by('data').filter(data__range=(data_ini, data_fim))
    
    @action(methods=['get'], detail=False)
    def intervalo(self, request, format=None):
        data_ini = self.request.query_params.get('data_ini')
        data_fim = self.request.query_params.get('data_fim')
        eventos = self.get_eventos(data_ini, data_fim)
        serializer = EventoSerializer(eventos, many=True)
        return Response(serializer.data)
