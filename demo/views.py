from django.shortcuts import render
from demo.forms import GeolocalisationForm

def index(request):
    geo_form = GeolocalisationForm(request.POST)

    if 'geom' in request.POST:
        if geo_form.is_valid():
            geo_form.save()

    return render(
        request,
        "demo/index.html",
        {
            "form": geo_form,
            "form_action": 'index',
        }
    )
