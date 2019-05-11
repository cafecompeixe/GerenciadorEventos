from rest_framework.viewsets import ModelViewSet
from presenca.api.serializers import PresencaSerializer
from presenca.models import Presenca

class PresencaViewSet(ModelViewSet):
    queryset=Presenca.objects.all()
    serializer_class = PresencaSerializer
