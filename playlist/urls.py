from django.conf.urls import url
from django.contrib import admin

from .views import * 
from django.contrib.auth.models import User

app_name = 'playlist'
urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^about/$', about, name='about'),
]

