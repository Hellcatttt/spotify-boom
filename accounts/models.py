from django.db import models
from django.contrib.auth.models import User

def upload_location(instance, filename):
    ProfileModel = instance.__class__
    if ProfileModel.objects.order_by("id").last():
        new_id = ProfileModel.objects.order_by("id").last().id + 1
    return "%s" %(filename)
 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE,related_name='profile')
    name = models.TextField(blank = True,null = True,default='name')
    mail = models.TextField(blank = True,null = True,default='mail')
    image = models.ImageField(upload_to=upload_location, blank = True,null = True)

