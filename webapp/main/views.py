# Create your views here.
# functions go here 

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from django.views.decorators.http import require_http_methods
from django.core import serializers
from models import Post
from django.shortcuts import render
from django.http import HttpResponseRedirect

def home(request):
	posts = Post.objects.all()
	postsjson = serializers.serialize('json', posts)
	return render_to_response('wendy_template.html',
                         dict(posts=postsjson),
                         context_instance=RequestContext(request))
 	#return render_to_response('wendy_template.html', { 'content': content })

def add(request):
    if request.method == 'POST': # If the form has been submitted...
		form = AddForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			title = request.POST['title']
			description = request.POST['description']
			return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = AddForm() # An unbound form

    return render(request, 'add.html', {
        'form': form,
    })