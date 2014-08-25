from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    
class Post(models.Model):
    category =  models.ForeignKey(Category, unique=False)
    user = models.ForeignKey(User, unique=False)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    # image = models.ImageField(upload_to='uploads/avatars', default='', blank=True)
   
    def __unicode__(self):
    	return self.name

admin.site.register(Category)
admin.site.register(Post)