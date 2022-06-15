from django import forms
from .models import grunge_artist, Album_grunge, Punk_artist, Album_punk, Funk_artist, Album_funk

class grunge_artistForm(forms.ModelForm):
    class Meta:
        model = grunge_artist
        fields = '__all__'
        widgets = {
            # 'name': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Nombre'}),
            # 'country': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Pais'}),
            # 'genre': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Genero'}),
        }

class album_grungeForm(forms.ModelForm):
    class Meta:
        model = Album_grunge
        fields = '__all__'
        widgets = {
            # 'title': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Titulo'}),
            # 'songs_number': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Numero de canciones'}),
            # 'launch_year': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Año de lanzamiento'}),
        }


class punk_artistForm(forms.ModelForm):
    class Meta:
        model = Punk_artist
        fields = '__all__'
        widgets = {
            # 'name': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Nombre'}),
            # 'country': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Pais'}),
            # 'genre': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Genero'}),
        }

class album_punkForm(forms.ModelForm):
    class Meta:
        model = Album_punk
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Titulo'}),
            'songs_number': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Numero de canciones'}),
            'launch_year': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Año de lanzamiento'}),
        }

class funk_artistForm(forms.ModelForm):
    class Meta:
        model = Funk_artist
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Nombre'}),
            'country': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Pais'}),
            'genre': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Genero'}),
        }

class album_funkForm(forms.ModelForm):
    class Meta:
        model = Album_funk
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Titulo'}),
            'songs_number': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Numero de canciones'}),
            'launch_year': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Año de lanzamiento'}),
        }