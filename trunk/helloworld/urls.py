# coding=utf-8
from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import *
from myapp import views
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


#sitemap
from myapp.sitemap import StaticSitemap
sitemaps = {
        'main':StaticSitemap,
        }

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'helloworld.views.home', name='home'),
    #url(r'^', include('myapp.urls')),
    url(r'^$', views.index),
    url(r'^add/$', views.add),
	url(r'^set_session/$', views.set_session),
    url(r'^search/$', views.search),
    url(r'^filters/$', views.getFilters),
    url(r'^google4d6b20cf8373e41a.html$', views.google),
    url(r'^api/jamu/$', views.jamuParse),
    # url(r'^parse/$', views.parse),
    #url(r'^index/$', views.test_template),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	
    #serve static files
	(r'^robots\.txt$', views.robots), 
#	(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),
#	(r'^robots.txt$', 'django.views.static.serve', { 'path' : '/static/robots.txt', 'document_root': settings.MEDIA_ROOT, 'show_indexes': False }), 
    (r'^content/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_CONTENT}),
    (r'^admin_static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ADMIN_STATIC}),
	#    (r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_IMAGES}),    
	(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)