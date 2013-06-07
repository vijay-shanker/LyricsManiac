from django.db import models

# Create your models here.
class Artist(models.Model):
    firstname = models.CharField(max_length=30)
    lastname  = models.CharField(max_length=30)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.firstname
    
class Genre(models.Model):
    name = models.CharField(max_length=60)
    about = models.TextField()
    
    def __str__(self):
        return self.name
    
class Band(models.Model):
    band = models.CharField(max_length=60)
    genre = models.ManyToManyField('Genre')
    artists = models.ManyToManyField('Artist')
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.band
    
class Album(models.Model):
    title = models.CharField(max_length=100)
    band  = models.ForeignKey('Band')
    released_date = models.DateTimeField(null=True, blank=True)
    genre = models.ManyToManyField('Genre')
    
    def __str__(self):
        return self.title

class Song(models.Model):
    song_title = models.CharField(max_length=100)
    lyrics = models.TextField()
    album = models.ForeignKey('Album')
    
    def __str__(self):
        return self.song_title
    

    
    

    
    
    
    

    

