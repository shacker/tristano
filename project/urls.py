from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User
from django.contrib import admin

from rest_framework import viewsets, routers

from profiles.views import ProfileDetailView, ProfileUpdateView, UserViewSet
from sampledata.views import BooksListView
from sampledata.views_api import BookViewSet
from sampledata.models import Book


admin.autodiscover()

# ViewSets define the API view behavior.
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

    # My Books
    url(r'^books/?$', BooksListView.as_view(),  name='books_list'),

    # API
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Home
    url(r'^$', 'main.views.home', name='home'),

)
