import settings
from django.conf.urls import patterns, include, url
from account.views import LoginView, RegisterView, logout_view, ResetPassword
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'auth/', include('social_auth.urls')),
    url(r'^$', LoginView.as_view(), name="login-view"),
    url(r'^register/$', RegisterView.as_view(), name="register-view"),
    url(r'^logout/$', logout_view, {'next_page': '/'}, name="logout-view"),
    #url(r'^signup/$', SignupView.as_view(), name="sign-up"),
    url(r'^lyrics/',include('lyrics.urls')),
    url(r'^reset_password',ResetPassword.as_view(), name="reset_password"),
    
    # url(r'^$', 'LyricsManiac.views.home', name='home'),
    # url(r'^LyricsManiac/', include('LyricsManiac.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))