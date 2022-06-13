from django.contrib import admin
from Artistas.models import album_funk, album_grunge, album_punk, funk_artist, punk_artist

from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(grunge_artist)
admin.site.register(album_grunge)
admin.site.register(punk_artist)
admin.site.register(album_punk)
admin.site.register(funk_artist)
admin.site.register(album_funk)






