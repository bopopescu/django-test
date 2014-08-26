from django.conf.urls import patterns, include, url
from registration.backends.default.views import RegistrationView
from userprofile.forms import UserRegistrationForm
from userprofile.models import UserProfile


urlpatterns = patterns('',
 
    # ...
    
    url(r'^accounts/register/$',RegistrationView,{'form_class' : UserRegistrationForm},name='registration_register'),
   
 
)