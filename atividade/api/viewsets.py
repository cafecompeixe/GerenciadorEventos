from rest_framework.viewsets import ModelViewSet
from atividade.api.serializers import AtividadeSerializer
from atividade.models import Atividade

class AtividadeViewSet(ModelViewSet):
    queryset=Atividade.objects.all()
    serializer_class = AtividadeSerializer
