from django.contrib import admin
from lyrics.models import Album, Artist, Band, Genre, Song
admin.site.register([Album,Artist,Band,Genre,Song])