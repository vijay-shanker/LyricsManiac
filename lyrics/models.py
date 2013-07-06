from django.db import models

# Create your models here.
class Artist(models.Model):
    firstname = models.CharField(max_length=30)
    lastname  = models.CharField(max_length=30)
    instrument = models.CharField(max_length=30)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.firstname + ' ' + self.lastname
    
class Genre(models.Model):
    name = models.CharField(max_length=60)
    about = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class Band(models.Model):
    band = models.CharField(max_length=60)
    genre = models.ManyToManyField('Genre',related_name='bands')
    artists = models.ManyToManyField('Artist')
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.band
    
    @property
    def copies_sold(self):
        albums = Album.objects.filter(band=self)
        num_copies = reduce(lambda x,y: x+y, albums.values_list('num_sold', flat=True))
        return num_copies
    
    
class Album(models.Model):
    title = models.CharField(max_length=100)
    band  = models.ForeignKey('Band', related_name= 'albums')
    release_date = models.DateTimeField(null=True, blank=True)
    genres = models.ManyToManyField('Genre', related_name='albums')
    num_sold = models.BigIntegerField(null=True, blank=True)
    price = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    @property
    def all_songs(self):
        all_songs = Song.objects.filter(album=self)
        return all_songs
    

class Song(models.Model):
    title = models.CharField(max_length=100)
    lyrics = models.TextField()
    album = models.ForeignKey('Album', related_name='songs')
    band = models.ForeignKey('Band', null=True, blank=True)
    
    def __str__(self):
        return self.title
    

    

    
    

    
    
    
    

    

