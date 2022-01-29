from django.db import models
from django.contrib.auth.models import User

def upload_location(instance, filename):
    AlbumModel = instance.__class__
    if AlbumModel.objects.order_by("id").last():
        new_id = AlbumModel.objects.order_by("id").last().id + 1
    return "%s" %(filename)

class Album(models.Model):
    name = models.TextField(blank = True,null = True,default='name')
    description = models.TextField(blank = True,null = True,default='mail')
    image = models.ImageField(upload_to=upload_location, blank = True,null = True)

