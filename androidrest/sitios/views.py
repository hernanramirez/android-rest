from rest_framework.viewsets import ModelViewSet
from .seliarizers import SitioSeralizer
from .models import Sitio

class SitioViewSet(ModelViewSet):
    queryset = Sitio.objects.all()
    serializer_class = SitioSeralizer
