# Create your views here.
# functions go here 

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from django.views.decorators.http import require_http_methods
from django.core import serializers
from models import Post
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
	#posts = Post.objects.all()
	posts = Post.objects.filter(user=request.user)
	postsjson = serializers.serialize('json', posts)
	return render_to_response('wendy_template.html',
                         dict(posts=postsjson),
                         context_instance=RequestContext(request))
 	#return render_to_response('wendy_template.html', { 'content': content })

@login_required
def marks(request):
	form = Post()
	if request.method == 'POST': # If the form has been submitted...
		form.title = request.POST['title']
		form.body = request.POST['body']
		form.lon = float(request.POST['lon'])
		form.lat = float(request.POST['lat'])
		form.user = request.user
		form.save()
		
	#return render(request, 'wendy_template.html', {
	#	'form': form,
	#})
	return redirect("/")