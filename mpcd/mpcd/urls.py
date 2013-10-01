from django.conf.urls import patterns, include, url
from mpcd.admin import admin_site
from django.http import HttpResponseRedirect

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mpcd.views.home', name='home'),
    # url(r'^mpcd/', include('mpcd.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^$', lambda r : HttpResponseRedirect('myadmin/')),
    url(r'myadmin/', include(admin_site.urls)),
    url(r'^default_admin/', include(admin.site.urls))
)
