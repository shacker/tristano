from django.http import HttpResponse
from profiles.models import Profile
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404

                
def profile_display(request, username=None):
    """
    A user's profile display
    """

    profile = get_object_or_404(Profile, user__username__iexact=username) 
    
    # items = Item.objects.filter(list=list,completed=False).order_by('priority','-created_date')
    
    return render_to_response(
    	"profiles/display.html",
    	locals()
    )    
    
