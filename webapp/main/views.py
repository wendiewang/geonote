# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader, RequestContext

def home(request):
	return render_to_response('wendy_template.html',
                         { },
                         context_instance=RequestContext(request))
	#return HttpResponse("Wendy Wang website coming soon!")


