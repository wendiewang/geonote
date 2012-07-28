# Create your views here.
# functions go here 


from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from django.views.decorators.http import require_http_methods
from django.core import serializers
from models import Post
from pymongo import Connection
import pymongo 




def home(request):
	posts = Post.objects.all()
	postsjson = serializers.serialize('json', posts)
	return render_to_response('wendy_template.html',
                         dict(posts=postsjson),
                         context_instance=RequestContext(request))
 	#return render_to_response('wendy_template.html', { 'content': content })


 	def connect_db(host, port, user, password, db_name):
    connect_string = "mongodb://%s:%s@%s:%d/%s" % \
            (user, password, host, port, db_name)

    c = pymongo.connection.Connection(connect_string)
    return c[db_name]

# def main():
#     global db
#     db = pymongo.connection.Connection("localhost")
#     db = connect_db("ds035907.mongolab.com", 35907, "geo_user", "password", "geodb")
#     db = db['geodb']
#     model.db = db

# if __name__ == '__main__':
# 	main()