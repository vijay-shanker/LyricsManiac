from django.contrib import admin
from lyrics.models import Album, Artist, Band, Genre, Song, Jargon, JargonThrough
admin.site.register([Album,Artist,Band,Genre, Jargon])

class JargonInline(admin.StackedInline):
    model = JargonThrough
    extra = 1
    
    
class SongAdmin(admin.ModelAdmin):
    inlines = [ JargonInline, ]
    
    
admin.site.register(Song, SongAdmin)

