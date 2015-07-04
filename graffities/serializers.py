from .models import Graffiti
from rest_framework.serializers import ModelSerializer


class GraffitiSerializer(ModelSerializer):
    class Meta:
        model = Graffiti
        exclude = ('active', 'checked', 'width', 'height')
