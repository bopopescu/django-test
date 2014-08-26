from django.conf.urls import patterns, include, url
from userprofile.forms import UserRegistrationForm
from userprofile.models import UserProfile


urlpatterns = patterns('',
 
    # ...
    
    url(r'^accounts/register/$',{'form_class' : UserRegistrationForm.as_view()},name='registration_register'),
   
 
)