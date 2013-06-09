# Create your views here.
from django.views.generic import ListView, DetailView
from django.shortcuts import get_list_or_404
from lyrics.models import Band, Album

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
    
    
    


