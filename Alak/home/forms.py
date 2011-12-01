from django import forms
from django.forms import ModelForm
from django.db import models as d_models
import re 
from django.contrib.auth.models import User
from django.template import Template, Context
from django.utils.safestring import mark_safe

from Alak.home import models
from Alak import settings
 
alnum_re = re.compile(r'^[\w.-]+$') # regexp. from jamesodo in #django  [a-zA-Z0-9_.]
alphanumric = re.compile(r"[a-zA-Z0-9]+$")
            
class LoginForm(forms.Form):
    username=forms.CharField(help_text='The username you were provided with')
    password=forms.CharField(widget=forms.PasswordInput, help_text='Your password')
    
class UpdateProfileForm(forms.Form):
    
    
    password       = forms.CharField  (min_length=6,
                                       max_length=30,
                                       widget=forms.PasswordInput,
                                       help_text='Enter a password that you can remember')
    password_again = forms.CharField  (max_length=30,
                                       widget=forms.PasswordInput,
                                       help_text='Enter the same password that you entered above')
    email          = forms.EmailField (help_text='Enter your e-mail address. eg, someone@gmail.com')
    display_name = forms.CharField(help_text = 'Your display name ' )
    photo = forms.CharField()
    room_number = forms.CharField()
    branch = forms.CharField()
    roll_number = forms.CharField()
    mobile_number = forms.CharField()
    about_me = forms.CharField(help_text = 'A few words about yourself' )
    
    class Meta:
        model = models.UserProfile
        fields=('display_name','password','password_again','photo','room_number','branch','email','roll_number','mobile_number','about_me')
        
    def clean_name(self):
	if not self.cleaned_data['name'].replace(' ','').isalpha():
	    raise forms.ValidationError(u'Names cannot contain anything other than alphabets.')
	else:
	    return self.cleaned_data['name']
	  
    
    def clean_email(self):
        return self.cleaned_data['email']
        

    def clean_password(self):
        if self.prefix:
            field_name1 = '%s-password'%self.prefix
            field_name2 = '%s-password_again'%self.prefix
        else:
            field_name1 = 'password'
            field_name2 = 'password_again'
            
        if self.data[field_name1] != '' and self.data[field_name1] != self.data[field_name2]:
            raise forms.ValidationError ("The entered passwords do not match.")
        else:
            return self.data[field_name1]