from django.http import HttpResponse
from profiles.models import Profile
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


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
        return render(
            request,
            "profiles/edit.html",
            locals()
        )

    except:
        return redirect('account_login')
