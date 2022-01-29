from django.db import models
from django.contrib.auth.models import User

def upload_location(instance, filename):
    ProfileModel = instance.__class__
    if ProfileModel.objects.order_by("id").last():
        new_id = ProfileModel.objects.order_by("id").last().id + 1
    return "%s" %(filename)
 
class Playlist(models.Model):
    name = models.TextField(blank = True,null = True,)
    image = models.ImageField(upload_to=upload_location, blank = True,null = True,)
    listenings = models.IntegerField(blank = True,null = True,)


class Track(models.Model):
    name = models.TextField(blank = True,null = True,default='My Playlist')
    artist = models.TextField(blank = True,null = True,default='My Playlist')
    listenings = models.IntegerField(blank = True,null = True,default=0)
    file = models.FileField(default='')