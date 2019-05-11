from rest_framework.serializers import ModelSerializer
from atividade.models import Atividade

class AtividadeSerializer(ModelSerializer):
    class Meta:
        model=Atividade
        fields=(
            "__all__"
        )

