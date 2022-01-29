from django.conf.urls import url
from django.contrib import admin

from .views import * 
from django.contrib.auth.models import User

app_name = 'albums'
urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^about/$', about, name='about'),
    url(r'^sign in/$', sing in, name='sign in'),
]