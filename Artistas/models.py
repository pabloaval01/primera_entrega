from pyexpat import model
from os import curdir
from django.db import models


# Create your models here.
class grunge_artist(models.Model): 
    name = models.CharField(max_length=40)
    country = models.CharField(max_length=25)
    genre = models.CharField(max_length=40)
    def __str__(self) -> str:
        return self.name+" - "+str(self.country)+" - " +str(self.genre)

class Album_grunge(models.Model):
    title = models.CharField(max_length=40)
    songs_number = models.IntegerField()
    launch_year = models.IntegerField()
    def __str__(self) -> str:
        return self.title+" - "+str(self.songs_number)+" - "+str(self.launch_year)

class Punk_artist(models.Model): 
    name = models.CharField(max_length=40)
    country = models.CharField(max_length=25)
    genre = models.CharField(max_length=40)
    def __str__(self) -> str:
        return self.name+" - "+str(self.country)+" - " +str(self.genre)

class Album_punk (models.Model):
    title = models.CharField(max_length=40)
    songs_number = models.IntegerField()
    launch_year = models.IntegerField()
    def __str__(self) -> str:
        return self.title+" - "+str(self.songs_number)+" - "+str(self.launch_year)

class Funk_artist(models.Model): 
    name = models.CharField(max_length=40)
    country = models.CharField(max_length=25)
    genre = models.CharField(max_length=40)
    def __str__(self) -> str:
        return self.name+" - "+str(self.country)+" - " +str(self.genre)

class Album_funk (models.Model):
    title = models.CharField(max_length=40)
    songs_number = models.IntegerField()
    launch_year = models.IntegerField()
    def __str__(self) -> str:
        return self.title+" - "+str(self.songs_number)+" - "+str(self.launch_year)


