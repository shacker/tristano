from django.conf.urls import patterns, include, url
from rest_framework import viewsets, routers
from profiles.views import profile_display, profile_edit
from django.contrib.auth.models import User
from sampledata.models import Book

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# ViewSets define the API view behavior.
class UserViewSet(viewsets.ModelViewSet):
    model = User

class BookViewSet(viewsets.ModelViewSet):
    model = Book

# Routers determine the URL conf for the API
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'books', BookViewSet)


urlpatterns = patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),

    # django-allauth
    (r'^accounts/', include('allauth.urls')),

    # User pages
    url(r'^p/edit/?$', profile_edit, name='profile_edit'),
    url(r'^p/(?P<username>\w+)/$', profile_display, name='profile_display'),

    # API
    url(r'^api/', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^$', 'main.views.home', name='home'),

)
