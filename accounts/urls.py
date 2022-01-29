from django.conf.urls import url
from django.contrib import admin

from .views import * #ALL
from django.contrib.auth.models import User

app_name = 'accounts'
urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^about/$', about, name='about'),
    url(r'^sign_in/$', sign_in, name='sign_in'),
    url(r'^api/register_user$', register_user, name='register_user'),
    url(r'^upload_track/$', upload_track_page, name='upload_track_page'),
    url(r'^api/upload_track/$', upload_track, name='upload_track'),
    url(r'^api/getplaylist/$', getplaylist, name='getplaylist'),

]