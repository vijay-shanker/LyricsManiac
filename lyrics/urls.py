from django.conf.urls import patterns, url
from lyrics.views import BandList, AlbumList

urlpatterns = patterns('',
    url(r'bands-list/$', BandList.as_view(), name="bands-list"),
    url(r'album-list/(?P<band_id>\d+)/$', AlbumList.as_view(), name="album-list")
    )