from django.conf.urls import patterns, include, url
from profiles.views import profile_display

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),

    # django-allauth
    (r'^accounts/', include('allauth.urls')),

    # User pages
    url(r'^p/(?P<username>\w+)/$', profile_display, name='profile_display'),

    url(r'^$', 'main.views.home', name='home'),

)
