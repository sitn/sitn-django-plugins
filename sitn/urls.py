from django.contrib import admin
from django.urls import include, path
from demo import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path("", views.index, name="index"),
]
