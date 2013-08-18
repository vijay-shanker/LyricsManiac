from django.conf.urls import patterns, url
from lyrics.views import BandList, AlbumList, LyricsView, EditLyrics
from django.contrib.auth.decorators import login_required
from lyrics.decorators import custom_login_dec

urlpatterns = patterns('',
    url(r'^bands-list/$', login_required(BandList.as_view(), login_url='/'), name="bands-list"),
    url(r'^album-list/(?P<band_id>\d+)/$', AlbumList.as_view(), name="album-list"),
    url(r'^show-lyrics/(?P<pk>\d+)/$',custom_login_dec(LyricsView.as_view()), name="lyrics-view"),
    url(r'^edit-lyrics/(?P<pk>\d+)/$',EditLyrics.as_view(), name="update-lyrics"),
    )