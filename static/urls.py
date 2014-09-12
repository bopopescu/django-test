#from django.conf.urls import patterns, url
from django.conf.urls.defaults import *
from django.contrib import admin
#from static import views

urlpatterns = patterns('',
   # ex: /polls/
   
    url(r'^$', views.index, name='index'),
)