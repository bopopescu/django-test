import json
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from category.models import Category,Post
from django.contrib import messages
import pdb;
def new(request):
    # If this is a post request we insert the person
   
    return render(request, 'create.html')
def create(request):
    # If this is a post request we insert the person
    if request.POST:
        cat = Category(
            name=request.POST['name'],
        )
        cat.save()

    categories = Category.objects.all()
    context = {'categories': categories}
    messages.add_message(request, messages.INFO, 'Category Create Succesfully')              
    return render(request, 'all_categories.html', context) 

def all_categories(request):
    # If this is a post request we insert the person
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'all_categories.html', context) 

def post_new(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'new_post.html', context)

def create_post(request):
    # If this is a post request we insert the person
    if request.POST:
        post = Post()
        post.name = request.POST['name']
        post.category_id = request.POST['category']
        post.user_id =  request.user.id
        post.save()
    posts = Post.objects.all()
  
    context = {'posts': posts}
    messages.add_message(request, messages.INFO, 'Post Succesfully')              
    return render(request, 'all_post.html', context) 


def all_posts(request):
    # If this is a post request we insert the person
    posts = Post.objects.all()
    context = {'posts': posts}
    return HttpResponseRedirect('category/all_posts/')


def my_posts(request):
    # If this is a post request we insert the person
    posts = request.user.post_set.order_by('-name')
    context = {'posts': posts}
    return render(request, 'my_post.html', context) 

def search_post(request):    # If this is a post request we insert the person
    posts = Post.objects.filter(name__icontains= request.POST['search'])
    context = {'posts': posts}
    return render(request, 'search_post.html', context) 
