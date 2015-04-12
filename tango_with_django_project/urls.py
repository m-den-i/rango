from django.conf.urls import patterns, include, url
from django.contrib import admin
from rango import views
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()
urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', include('rango.urls')),
                       url(r'^accounts/', include('allauth.urls')),
                       )
if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
                            url(r'^media/(?P<path>.*)',
                                'serve',
                                {'document_root': settings.MEDIA_ROOT}))
urlpatterns += patterns(
    'django.contrib.auth.views',

    url(r'^login/$', 'login',
        {'template_name': 'demo/login.html'},
        name='user_login'),
    url(r'^logout/$', 'logout',
        {'next_page': 'index'},
        name='user_logout'),
)