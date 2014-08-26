"""
Django settings for post project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!iq#$h(701s!j7sgs!gs0$dv0zlk4=fvj1&tphb8)767m=@nvt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

FACEBOOK_APP_ID = '282925365146253'
FACEBOOK_SECRET_KEY = 'd74b3dc23c98f6e6a145afb5219e6e5f'
TWITTER_KEY = 'FOQTqF1JWQw5OmuPxr5xMg'
TWITTER_SECRET = 'Bbk9b84stzpk5OmaM6O06X6IpjJKnZd8Q8FNJ2iXIo'
TWITTER_OAUTH_TOKEN = '537084108-tB7nEfQBcOE7DO20OxSJoPm87IXfuYZSZlTmaLb2'
TWITTER_OAUTH_TOKEN_SECRET = 'dIUR0XHySaRBz0T0nC95NLgw1c3IvBAZpuNqfcws'


ACCOUNT_ACTIVATION_DAYS=7
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'hitesh.gurjar786@gmail.com'
EMAIL_HOST_PASSWORD = 'H!tesh@#$88'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', ]
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'post',
    'django.contrib.humanize',
    'static',
    'category',
    'jquery',
    'userprofile',
    'south',
    'bootstrap3'
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'post.urls'

WSGI_APPLICATION = 'post.wsgi.application'
TEMPLATE_DIRS = (
   '/home/yuva/Desktop/python/post/templates'
)


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3456'),
        
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
#MEDIA_URL = 'http://localhost:8000/' 
#STATIC_ROOT =  os.path.join("/home/yuva/Desktop/python/post/", 'static')
STATIC_ROOT = os.path.join(PROJECT_ROOT,'static/')
STATIC_URL = '/static/'
import django.contrib.auth
django.contrib.auth.LOGIN_URL = '/'
AUTH_PROFILE_MODULE='userprofile.UserProfile'

BOOTSTRAP3 = {
'set_required': False,
'error_css_class': 'bootstrap3-error',
'required_css_class': 'bootstrap3-required',
'javascript_in_head': True,
}

