from django.http import HttpResponse  # Import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso # Importar el modelo
from django.template import loader # Importar el loader
 
 # Importar render

# Create your views here.

def curso(self):
    curso = Curso(nombre="Desarrollo Web", camada=16740) 
    curso.save()
    documento =f"Curso: {curso.nombre} - Camada: {curso.camada}"
    return HttpResponse(documento)

def profesores(self):
    documento = f"Pagina de Profesores"
    return HttpResponse(documento)

def inicio(self):
    plantilla = loader.get_template('inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)