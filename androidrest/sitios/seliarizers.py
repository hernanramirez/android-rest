from rest_framework.serializers import ModelSerializer
from .models import Sitio

class SitioSeralizer(ModelSerializer):
    class Meta:
        model = Sitio
