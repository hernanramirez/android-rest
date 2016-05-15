from django.db import models

from versatileimagefield.fields import VersatileImageField

class Sitio(models.Model):
    nombre = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()
    sitio_image = VersatileImageField(
        'Imagen del sitio',
        upload_to='images_sitios/'
    )
