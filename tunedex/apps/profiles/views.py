from profiles.models import Profile
from django.shortcuts import render, get_object_or_404


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
