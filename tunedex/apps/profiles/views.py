from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.html import strip_tags


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
