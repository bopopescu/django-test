from django import forms
from userprofile.models import UserProfile
from registration.forms import RegistrationForm
from django.utils.translation import ugettext_lazy as _
import pdb;


attrs_dict = { 'class': 'optinal' }


class UserRegistrationForm(RegistrationForm):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    
RegistrationForm.base_fields.update(UserRegistrationForm.base_fields)
