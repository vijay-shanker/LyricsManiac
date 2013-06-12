# Create your views here.
#from utils.urlconf import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView
from django.shortcuts import get_list_or_404, get_object_or_404, redirect
from lyrics.models import Band, Album, Song
from django import forms
from django.core.urlresolvers import reverse

class UpdateLyricsForm(forms.ModelForm):
    class Meta:
        model= Song
        
    

class BandList(ListView):
    model = Band
    template_name =  'lyrics/bandlist.html'
    context_object_name = 'bandlist'
    
    def get_context_data(self, **kwargs):
        context = super(BandList,self).get_context_data(**kwargs)
        return context
    
class AlbumList(DetailView):
    model = Album
    template_name = 'lyrics/albumlist.html'
    context_object_name = 'albumlist'
    
    def get_object(self, queryset=None):
        return get_list_or_404(Album, band__id = self.kwargs['band_id'])

class LyricsView(DetailView):
    model = Song
    template_name = 'lyrics/lyrics.html'
    context_object_name = 'lyrics'
    
    def get_object_name(self):
        return get_object_or_404(Song, id = self.kwargs['pk'])
    
class EditLyrics(UpdateView):
    template_name = 'lyrics/update_lyrics.html'
    form_class = UpdateLyricsForm
    
    def get_object(self):
        return Song.objects.get(pk=self.kwargs['pk'])
    
    def get_success_url(self):
        return reverse('lyrics-view', args=(self.kwargs.get('pk'),))
    
    

        
    

    
    
    


