from django.shortcuts import render_to_response
from django.template import RequestContext        

def home(request):
    """
    Homepage view
    """
    
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))