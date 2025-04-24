from django.contrib.gis import admin
from .models import DemoPoint
from django_extended_ol.admin import WMTSGISWithSearchModelAdmin

admin.site.register(DemoPoint, WMTSGISWithSearchModelAdmin)
