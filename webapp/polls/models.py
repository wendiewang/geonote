from django.db import models
import datetime
from django.utils import timezone

# If you make any changes to this file, you need to rerun the following commands 
# python manage.py sql polls 
# python manage.py syncdb 
# python manage.py runserver # restart the server 

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=600)
    pub_date = models.DateTimeField()
    lon = models.FloatField()
    lat = models.FloatField()

# class Poll(models.Model):
#     question = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     def __unicode__(self):
#     	return self.question
#     def was_published_recently(self):
#     	return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# class Choice(models.Model):
#     poll = models.ForeignKey(Poll)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField()
#     def __unicode__(self):
#     	return self.choice_text

# class WorldBorder(models.Model):
#     # Regular Django fields corresponding to the attributes in the
#     # world borders shapefile.
#     name = models.CharField(max_length=50)
#     area = models.IntegerField()
#     pop2005 = models.IntegerField('Population 2005')
#     fips = models.CharField('FIPS Code', max_length=2)
#     iso2 = models.CharField('2 Digit ISO', max_length=2)
#     iso3 = models.CharField('3 Digit ISO', max_length=3)
#     un = models.IntegerField('United Nations Code')
#     region = models.IntegerField('Region Code')
#     subregion = models.IntegerField('Sub-Region Code')
#     lon = models.FloatField()
#     lat = models.FloatField()

#     # GeoDjango-specific: a geometry field (MultiPolygonField), and
#     # overriding the default manager with a GeoManager instance.
#     mpoly = models.MultiPolygonField()
#     objects = models.GeoManager()

#     # Returns the string representation of the model.
#     def __unicode__(self):
#         return self.name