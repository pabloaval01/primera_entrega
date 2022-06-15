from django.contrib import admin
from Artistas.models import  Album_grunge, Album_punk, Funk_artist, Punk_artist, Album_funk

from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(grunge_artist)
admin.site.register(Album_grunge)
admin.site.register(Punk_artist)
admin.site.register(Album_punk)
admin.site.register(Funk_artist)
admin.site.register(Album_funk)






