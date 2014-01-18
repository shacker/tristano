from django.conf.urls import patterns, include, url
from rest_framework import viewsets, routers
from profiles.views import ProfileDetailView, ProfileUpdateView
from django.contrib.auth.models import User
from sampledata.models import Book
from sampledata.views import BookViewSet

from django.contrib import admin
admin.autodiscover()

# ViewSets define the API view behavior.
class UserViewSet(viewsets.ModelViewSet):
    model = User



# Routers determine the URL conf for the API
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'books', BookViewSet)


urlpatterns = patterns('',

	# Admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    # django-allauth -- registration, login, passwords
    (r'^accounts/', include('allauth.urls')),

    # Profiles
    url(r'^p/edit/?$', ProfileUpdateView.as_view(),  name='profile_update'),
    url(r'^p/(?P<username>\w+)/$', ProfileDetailView.as_view(),  name='profile_detail'),

    # API
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Home
    url(r'^$', 'main.views.home', name='home'),

)
