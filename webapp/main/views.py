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
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.contrib.auth.forms import UserCreationForm

# decorator 
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
		form.img = request.FILES['file']
		form.user = request.user
		form.save()
	return redirect('/')
            
def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			# new_user = User()
			# new_user.username = form.cleaned_data['username']
			# new_user.setPassword(form.cleaned_data['password'])
			# new_user.save()
			new_user = form.save()
			user = authenticate(username=new_user.username, password=form.cleaned_data['password1'])
			login(request, user)
			return redirect("/")
	else:
		form = UserCreationForm()
	return render_to_response("registration/register.html", dict(form=form), 
		context_instance=RequestContext(request))

# def user_login(request):
#     username = request.POST.get("user")
#     print username
#     password = request.POST.get("password")
#     print password
#     user = authenticate(username=username, password=password)

#     if user:
#         print("Successfully logged in")
#         login(request, user)
#         return redirect("home")
#     else:
#         print "No such user"
#         return render(request, "bad_login.html")

# def user_logout(request):
#     logout(request)
#     return redirect("home")
