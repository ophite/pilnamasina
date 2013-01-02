# coding=utf-8
from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from myapp import views
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'helloworld.views.home', name='home'),
    #url(r'^', include('myapp.urls')),
    url(r'^$', views.index),
    url(r'^add/$', views.add),
	url(r'^set_session/$', views.set_session),
    url(r'^search/$', views.search),
    #url(r'^index/$', views.test_template),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),

    #serve static files
    (r'^content/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_CONTENT}),
    (r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_IMAGES}),    
)