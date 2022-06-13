from django.urls import path
from Artistas.views import album_grungeFormView, grunge_artists, grunge_artistFormView, album_grunge, album_grungeFormView, album_punk, album_punkFormView, punk_artist, punk_artistFormView, album_funk, album_funkFormView, funk_artist, funk_artistFormView
from Artistas.views import album_grunge
from Artistas.views import punk_artist
from Artistas.views import album_punk
from Artistas.views import funk_artist
from Artistas.views import album_funk
from Artistas.views import inicio
from Artistas.views import description
from Artistas.views import grunge_artistForm
from Artistas.views import album_grungeForm 
from Artistas.views import album_punkForm
from Artistas.views import punk_artistForm  
from Artistas.views import album_funkForm 
from Artistas.views import funk_artistForm
from Artistas.views import description
from Artistas.views import searchGrungeArtist
from Artistas.views import searchGrungeArtist_result 

urlpatterns = [
    path('description/', description, name='description'),
    path('grungeArtist/', grunge_artists, name='grungeArtists'),
    path('grungeAlbum/', album_grunge, name='grungeAlbum'),
    path('punkArtist/', punk_artist, name='punkArtist'),
    path('punkAlbum/', album_punk, name='punkAlbum'),
    path('funkArtist/', funk_artist, name='funkArtist'),
    path('funkAlbum/', album_funk, name='funkAlbum'),
    path('', inicio, name='inicio'),

    path('grungeArtistForm/', grunge_artistFormView, name='grungeArtistForm'),
    path('albumGrungeForm/', album_grungeFormView, name='albumGrungeForm'),
    path('punkArtistForm/', punk_artistFormView, name='punkArtistForm'),
    path('albumPunkForm/', album_punkFormView, name='albumPunkForm'),
    path('funkArtistForm/', funk_artistFormView, name='funkArtistForm'),
    path('albumFunkForm/', album_funkFormView, name='albumFunkForm'),

    path('searchGrungeArtist/', searchGrungeArtist, name='searchGrungeArtist'),
    path('searchGrungeArtist_result/', searchGrungeArtist_result, name='searchGrungeArtist_result'),
    

    
]