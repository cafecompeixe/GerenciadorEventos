from rest_framework.viewsets import ModelViewSet
from core.api.serializers import EventoSerializer
from core.models import Evento

class EventoViewSet(ModelViewSet):
    queryset=Evento.objects.all()
    serializer_class = EventoSerializer
