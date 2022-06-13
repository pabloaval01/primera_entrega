from cmath import e
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from Artistas.forms import grunge_artistForm, album_grungeForm, punk_artistForm, album_punkForm, funk_artistForm, album_funkForm, grunge_artist

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
        return render(request,'artistas/searchGrungeArtist_result.html', {'name':name})
    else:
        response = "asd"
    return render(request,'artistas/searchGrungeArtist.html')
