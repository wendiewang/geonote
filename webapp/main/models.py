from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
# only functions that are used for manipulating data from the database 

class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    lon = models.FloatField(max_length=10)
    lat = models.FloatField(max_length=10)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

# class UserProfile(models.Model):
# 	user = models.OneToOneField(User)