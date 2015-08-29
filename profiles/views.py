from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, UpdateView

from rest_framework import viewsets

from profiles.models import Profile
from profiles.forms import ProfileForm
from profiles.serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint presents the users in the system.

    The collection of book instances owned by a user are
    serialized using a hyperlinked representation, via this connection.

    n.b. This should prob. be in a separate `users` app but makes sense in profiles.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer



class ProfileDetailView(DetailView):

    def get_object(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return user.profile


class ProfileUpdateView(UpdateView):

    model = Profile
    form_class = ProfileForm

    def get_object(self):
        return self.request.user.profile

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.get_object())

        if form.is_valid():
            instance = form.save(commit=False)
            instance.bio = strip_tags(form.cleaned_data['bio'])
            instance.influences = strip_tags(form.cleaned_data['influences'])
            instance.save()

            messages.add_message (request, messages.SUCCESS, 'Profile saved!')
            url = reverse('profile_detail', kwargs={'username': request.user.username})
            return HttpResponseRedirect(url)
        else:
            # No required fields here...
            pass
