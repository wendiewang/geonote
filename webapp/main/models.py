from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
# only functions that are used for manipulating data from the database 

class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    lon = models.FloatField(max_length=10)
    lat = models.FloatField(max_length=10)
    img = models.FileField(blank=True, null=True, upload_to='.')
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

class UserProfile(models.Model):
 	user = models.OneToOneField(User)
 	img = models.FileField(blank=True, null=True, upload_to='.')

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)