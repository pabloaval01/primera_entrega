from cmath import e
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from Artistas.forms import grunge_artistForm, punk_artistForm, album_punkForm, funk_artistForm, album_funkForm, grunge_artist, album_grungeForm
from Artistas.models import Album_grunge, Punk_artist, Album_punk, Funk_artist, Album_funk

# Create your views here.
def description(request):
    document = f"Description Page"
    return render(request,'Artistas/description.html')

def grunge_artists(request):
    document = f"Grunge Artists Page"
    return render(request,'Artistas/grungeArtist.html')

def album_grunge(request):
    document = f"Grunge Albun's Page"
    return render(request,'artistas/grungeAlbum.html')

def punk_artist(request):
    document = f"Punk Artists Page"
    return render(request,'artistas/punkArtist.html')

def album_punk(request):
    document = f"Punk Albun's Page"
    return render(request,'artistas/punkAlbun.html')

def funk_artist(request):
    document = f"Funk Artists Page"
    return render(request,'artistas/funkArtist.html')

def album_funk(request):
    document = f"Funk Albun's Page"
    return render(request,'artistas/funkAlbun.html')

def inicio(self):
    template = loader.get_template('artistas/home.html')
    document = template.render()
    return HttpResponse(document)

def grunge_artistFormView(request):
    if request.method == 'POST':
        myform = grunge_artistForm(request.POST)
        if myform.is_valid():
            information = myform.cleaned_data
            myform.save()
        return render(request,'artistas/home.html')
    else:
        myform = grunge_artistForm()
        return render(request,'artistas/grungeArtistForm.html', {'myform':myform})
    
def album_grungeFormView(request):
    if request.method == 'POST':
        albumGrunge = album_grungeForm(request.POST)
        if albumGrunge.is_valid():
            information = albumGrunge.cleaned_data
            albumGrunge.save()
        return render(request,'artistas/home.html')
    else:
        albumGrunge = album_grungeForm()
        return render(request,'artistas/grungeAlbumForm.html', {'albumGrunge':albumGrunge})

def punk_artistFormView(request):
    if request.method == 'POST':
        punkArtist = punk_artistForm(request.POST)
        if punkArtist.is_valid():  
            information = punkArtist.cleaned_data 
            punkArtist.save()   
        return render(request,'artistas/home.html')
    else:
        punkArtist = punk_artistForm()
        return render(request,'artistas/punkArtistForm.html', {'punkArtist':punkArtist})

def album_punkFormView(request):
    if request.method == 'POST':
        albumPunk = album_punkForm(request.POST)
        if albumPunk.is_valid():
            information = albumPunk.cleaned_data
            albumPunk.save()
        return render(request,'artistas/home.html')
    else:
        albumPunk = album_punkForm()
        return render(request,'artistas/punkAlbumForm.html', {'albumPunk':albumPunk})

def funk_artistFormView(request):
    if request.method == 'POST':
        funkArtist = funk_artistForm(request.POST)
        if funkArtist.is_valid():  
            information = funkArtist.cleaned_data 
            funkArtist.save()   
        return render(request,'artistas/home.html')
    else:
        funkArtist = funk_artistForm()
        return render(request,'artistas/funkArtistForm.html', {'funkArtist':funkArtist})

def album_funkFormView(request):
    if request.method == 'POST':
        albumFunk = album_funkForm(request.POST)
        if albumFunk.is_valid():
            information = albumFunk.cleaned_data
            albumFunk.save()
        return render(request,'artistas/home.html')
    else:
        albumFunk = album_funkForm()
        return render(request,'artistas/funkAlbumForm.html', {'albumFunk':albumFunk})


def searchGrungeArtist(request):
    return render(request,'artistas/searchGrungeArtist.html')

def searchGrungeArtist_result(request):
    if request.GET['name']:
        name = request.GET["name"]
        artist = grunge_artist.objects.filter(name__icontains=name)
        return render(request,'artistas/searchGrungeArtist_result.html', {'name':artist})
    else:
        response = "Serch artist by name"
    return render(request,'artistas/searchGrungeArtist.html')


def searchGrungeAlbum(request):
    return render(request,'artistas/searchGrungeAlbum.html')

def searchGrungeAlbum_result(request):
    if request.GET['title']:
        title = request.GET["title"]
        album = Album_grunge.objects.filter(title__icontains=title)
        return render(request,'artistas/searchGrungeAlbum_result.html', {'title':album})
    else:
        response = "Serch album's by name"
    return render(request,'artistas/searchGrungeAlbum.html')


def searchPunkArtist(request):
    return render(request,'artistas/searchPunkArtist.html')

def searchPunkArtist_result(request):
    if request.GET['name']:
        name = request.GET["name"]
        artist = Punk_artist.objects.filter(name__icontains=name)
        return render(request,'artistas/searchPunkArtist_result.html', {'name':artist})
    else:
        response = "Serch artist by name"
    return render(request,'artistas/searchPunkArtist.html')


def searchPunkAlbum(request):
    return render(request,'artistas/searchPunkAlbum.html')

def searchPunkAlbum_result(request):
    if request.GET['title']:
        title = request.GET["title"]
        album = Album_punk.objects.filter(title__icontains=title)
        return render(request,'artistas/searchPunkAlbum_result.html', {'title':album})
    else:
        response = "Serch album's by name"
    return render(request,'artistas/searchPunkAlbum.html')

####

def searchFunkArtist(request):
    return render(request,'artistas/searchFunkArtist.html')

def searchFunkArtist_result(request):
    if request.GET['name']:
        name = request.GET["name"]
        artist = Funk_artist.objects.filter(name__icontains=name)
        return render(request,'artistas/searchFunkArtist_result.html', {'name':artist})
    else:
        response = "Serch artist by name"
    return render(request,'artistas/searchFunkArtist.html')


def searchFunkAlbum(request):
    return render(request,'artistas/searchFunkAlbum.html')

def searchFunkAlbum_result(request):
    if request.GET['title']:
        title = request.GET["title"]
        album = Album_funk.objects.filter(title__icontains=title)
        return render(request,'artistas/searchFunkAlbum_result.html', {'title':album})
    else:
        response = "Serch album's by name"
    return render(request,'artistas/searchFunkAlbum.html')