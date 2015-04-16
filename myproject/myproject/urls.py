from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    
    url(r'^update$', "contentAppBarrapunto.views.update"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(.*)$', "contentAppBarrapunto.views.serve"),
)
