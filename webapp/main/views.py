# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from django.views.decorators.http import require_http_methods
from models import Post

#@require_http_methods(["POST"])
# def home(request):
# 	content = "hello"
# 	return render_to_response('wendy_template.html',{ 'content': content })

def home(request):
	post = Post.objects.get(id=2)
	return render_to_response('wendy_template.html',
                         dict(post=post), 
                         context_instance=RequestContext(request))