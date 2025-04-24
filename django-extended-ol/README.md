# django-extended-ol

django-extended-ol is a Django app that extends the basic OpenLayers Widget.

Features:

* Custom WMTS base_layer with fixed resolutions
* Search on the map (third-party service needed)

## Quick start

```sh
pip install django-extended-ol
```

1. Add "django_extended_ol" to your INSTALLED_APPS setting like this:

```python
INSTALLED_APPS = [
    ...,
    "django_extended_ol",
]
```

2. Configure django_extended_ol in your settings.py, here's an example:

```python
OLWIDGET = {
    "globals": {
        "srid": 2056,
        "default_center": [2551470, 1211190], # optional
        "default_resolution": 18, # optional
        "extent": [2420000, 1030000, 2900000, 1360000],
        "resolutions": [250, 100, 50, 20, 10, 5, 2.5, 2, 1.5, 1, 0.5, 0.25, 0.125, 0.0625]
    },
    "wmts": {
        "layer_name": 'plan_cadastral',
        "style": 'default',
        "matrix_set": 'EPSG2056',
        "attributions": '<a target="new" href="https://sitn.ne.ch/web/conditions_utilisation/contrat_SITN_MO.htm'
            + '">© SITN</a>', # optional
        "url_template": 'https://sitn.ne.ch/mapproxy95/wmts/1.0.0/{layer}/{style}/{TileMatrixSet}/{TileMatrix}/{TileRow}/{TileCol}.png',
        "request_encoding": 'REST', # optional
        "format": 'image/png' # optional
    },
    "search": { # optional, only if you want a search service
        "url_template": 'https://sitn.ne.ch/search?limit=10&partitionlimit=2&interface=desktop&query={search_term}'
    }
}
```

3. You can now use `WMTSWidget` in your gis forms:

```python
from django_extended_ol.forms.widgets import WMTSWidget
...
class MyCustomGISClass:
    gis_widget = WMTSWidget
```

If you want a search widget, you can use `WMTSWithSearchWidget`. Please check search service specification below.

4. You can also use it in your admin.py:

```python
from django.contrib.gis import admin
from .models import YourGeomModel
from olwidget.admin import WMTSGISModelAdmin

admin.site.register(YourGeomModel, WMTSGISModelAdmin)
```

If you want the search widget please use `WMTSGISWithSearchModelAdmin`. Please check search service specification below.

5. Start the development server and visit the admin.


## Search service specification

You'll need a templated URL as showcased in the `settings.py` above.
Such service should reply GeoJSON feature collection and each feature should have a `bbox` and a property named `label`.
