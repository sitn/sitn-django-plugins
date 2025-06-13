from django.contrib.gis import forms
from django_extended_ol.forms.widgets import WMTSWithSearchWidget, WMTSWidget

from demo.models import DemoPoint


class GeolocalisationForm(forms.ModelForm):
    geom = forms.PointField(widget=WMTSWithSearchWidget(attrs={"geom": ""}))
    class Meta: 
        model = DemoPoint
        fields = "__all__"
