from django.db import models
# Create your models here.
# only functions that are used for manipulating data from the database 


class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


