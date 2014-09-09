from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.utils import simplejson as json
from userprofile.models import UserProfile
from twython import Twython, TwythonError
import pdb;
import httplib2
import urllib
# Create your views here.
def index(request):
    latest_poll_list = "hi how are you"
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'static/index.html', context)

def facebook(request):
    params = {
        'client_id': settings.FACEBOOK_APP_ID,
        'redirect_uri': 'http://localhost:8000/facebook/',
        'client_secret': settings.FACEBOOK_SECRET_KEY,
        'code': request.GET['code']
    }

    http = httplib2.Http(timeout=15)
    response, content = http.request('https://graph.facebook.com/oauth/access_token?%s' % urllib.urlencode(params))
    
    # Find access token and expire (this is really gross)
    params = content.split('&')
    ACCESS_TOKEN = params[0].split('=')[1]
    EXPIRE = params[1].split('=')[1]
    
    # Get basic information about the person
    response, content = http.request('https://graph.facebook.com/me?access_token=%s' % ACCESS_TOKEN)
    data = json.loads(content)
    # Try to find existing profile, create a new user if one doesn't exist
    try:
        profile = UserProfile.objects.get(facebook_uid=data['id'])
    except UserProfile.DoesNotExist:
        user = User.objects.get_or_create(username= data['username'],first_name = data['first_name'],last_name=data['last_name'])
        user = User.objects.get(username=data['username'])
        profile = UserProfile(user = user)
        profile.facebook_uid = data['id']

    # Update token and expire fields on profile
    profile.facebook_access_token = ACCESS_TOKEN
    profile.facebook_access_token_expires = EXPIRE
    profile.save()
    # Authenticate and log user in
    #user = authenticate(username=profile.user.username, password='')
    user =profile.user
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    auth_login(request, user)
    
    return HttpResponseRedirect('/')


def twitter_login(request):
    twitter = Twython(settings.TWITTER_KEY,  settings.TWITTER_SECRET)
    auth_props = twitter.get_authentication_tokens()
    request.session['oauth_token'] = auth_props['oauth_token']
    request.session['oauth_token_secret'] = auth_props['oauth_token_secret']
    return HttpResponseRedirect("/twitter/callback/")


def twitter_callback(request):

    twitter = Twython(settings.TWITTER_KEY, settings.TWITTER_SECRET, TWITTER_OAUTH_TOKEN,request.session.get('oauth_token_secret'),)
    authorized_tokens = twitter.get_authorized_tokens(request.GET.get('oauth_verifier'))
    try:
        profile = UserProfile.objects.get(screen_name = authorized_tokens['screen_name'])
        user = User.objects.get(pk=profile.user_id)
        user.backend = 'django.contrib.auth.backends.ModelBackend'

        if user.is_active:
            auth_login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/accounts/login/')
    except UserProfile.DoesNotExist:
        name = authorized_tokens['screen_name'],
        oauth_token = authorized_tokens['oauth_token'],
        oauth_token_secret = authorized_tokens['oauth_token_secret'],
       
        user = add_user(
            name, oauth_token_secret, "fjdsfn@jfndjfn.com"
        )
       
        create_twitter_profile(
            user.id, oauth_token, oauth_token_secret, name
        )
       
        user = authenticate(
            username=name, password=oauth_token_secret
        )
       
        auth_login(request, user)
       
        return HttpResponseRedirect('/')
       

def create_twitter_profile(id, oauth_token, oauth_token_secret, name):
    profile = UserProfile()
    profile.user_id = id
    profile.oauth_token = oauth_token
    profile.oauth_secret = oauth_token_secret
    profile.screen_name = name
    profile.save()
   
   
def add_user(username, password, email):
    user = User.objects.create_user(
        username=username,
        password=password,
        email=email
    )
    user.is_active = True
    user.save()
    return user



