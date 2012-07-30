# Create your views here.
# functions go here 

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from django.views.decorators.http import require_http_methods
from django.core import serializers
from models import Post

def home(request):
	posts = Post.objects.all()
	postsjson = serializers.serialize('json', posts)
	return render_to_response('wendy_template.html',
                         dict(posts=postsjson),
                         context_instance=RequestContext(request))
 	#return render_to_response('wendy_template.html', { 'content': content })
