from django.contrib import admin
from django.urls import path, include
from Artistas.views import grunge_artists, album_grunge, punk_artist, album_punk, funk_artist, album_funk
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Artistas.urls')),
]
