from django.conf import settings
from django.contrib.gis.db import models


class DemoPoint(models.Model):
    name = models.CharField(max_length=50)
    geom = models.PointField(srid=settings.DEFAULT_SRID)
