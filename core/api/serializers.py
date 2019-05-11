from rest_framework.serializers import ModelSerializer
from core.models import Evento

class EventoSerializer(ModelSerializer):
    class Meta:
        model=Evento
        fields=(
            "__all__"
        )

