from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from registration.signals import user_registered
import pdb;


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to='uploads/avatars', default='', blank=True)
    facebook_uid = models.PositiveIntegerField(blank=True, null=True)
    facebook_access_token = models.CharField(blank=True, max_length=255)
    facebook_access_token_expires = models.PositiveIntegerField(blank=True, null=True)
    oauth_token = models.CharField(max_length=200)
    oauth_secret = models.CharField(max_length=200)
    screen_name = models.CharField(max_length=50,blank=True, null=True  )
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.first_name

def user_registered_callback(sender, user, request, **kwargs):
    profile = UserProfile(user = user)
    profile.first_name = request.POST["first_name"]
    profile.last_name = request.POST["last_name"]
    user.first_name= request.POST["first_name"]
    user.last_name = request.POST["last_name"]
    profile.save()
    user.save()

user_registered.connect(user_registered_callback)