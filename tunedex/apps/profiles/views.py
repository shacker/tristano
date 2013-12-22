from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from profiles.models import Profile
from profiles.forms import ProfileForm


def profile_display(request, username=None):
    """
    A user's profile display
    """

    profile = get_object_or_404(Profile, user__username__iexact=username)

    return render(
    	request,
    	"profiles/display.html",
    	locals()
    )


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
        print "posting"
        form = ProfileForm(instance=profile, data=request.POST)
        print form
        if form.is_valid():
            print "valid"
            form.save()
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