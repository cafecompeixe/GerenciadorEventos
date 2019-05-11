from rest_framework.serializers import ModelSerializer
from presenca.models import Presenca

class PresencaSerializer(ModelSerializer):
    class Meta:
        model=Presenca
        fields=(
            "__all__"
        )

