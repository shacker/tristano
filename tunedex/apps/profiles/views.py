from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from django.views.generic import DetailView

from profiles.models import Profile
from profiles.forms import ProfileForm


class ProfileDetailView(DetailView):

    # No need to specify context_object_name = 'profile' for template - it's implied

    def get_object(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return user.profile


def profile_edit(request):
    """
    User edits own profile
    """

    try:
        profile = Profile.objects.get(user__username__iexact=request.user.username)
        form = ProfileForm(instance=profile)
    except:
        return redirect('account_login')

    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():

            # Strip out all HTML; we allow markdown only
            uprofile = form.save(commit=False)
            uprofile.bio = strip_tags(form.cleaned_data['bio'])
            uprofile.influences = strip_tags(form.cleaned_data['influences'])
            uprofile.save()

            messages.add_message (request, messages.SUCCESS, 'Profile saved!')
            url = reverse('profile_display', kwargs={'username': request.user.username})
            return HttpResponseRedirect(url)
    else:
        form = ProfileForm(instance=profile)

    return render(
        request,
        "profiles/edit.html",
        locals()
    )
