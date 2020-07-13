from django.contrib.gis import admin
from .models import Camera

admin.site.register(Camera,admin.OSMGeoAdmin)
