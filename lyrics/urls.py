from django.conf.urls import patterns, url
from lyrics.views import BandList, AlbumList, LyricsView

urlpatterns = patterns('',
    url(r'bands-list/$', BandList.as_view(), name="bands-list"),
    url(r'album-list/(?P<band_id>\d+)/$', AlbumList.as_view(), name="album-list"),
    url(r'show-lyrics/(?P<pk>\d+)/$',LyricsView.as_view(), name="lyrics-view"),
    )