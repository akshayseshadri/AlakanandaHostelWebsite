from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import auth
from django.contrib.auth.models import User, Group
from django.template.loader import get_template
from django.template.context import Context, RequestContext
from django.utils.translation import ugettext as _
from django.core.mail import send_mail,EmailMessage,SMTPConnection
from django.contrib.sessions.models import Session
from django.utils import simplejson

from Alak.misc.util import *
from Alak.settings import *
from Alak.home.models import *
from Alak.home import forms
import sha,random,datetime

def login (request):
       
    form=forms.LoginForm()
    if 'logged_in' in request.session and request.session['logged_in'] == True:
	return HttpResponseRedirect("%shome_page/" % settings.SITE_URL)	            
            
    if request.method == 'POST':
        data = request.POST.copy()
        form = forms.LoginForm(data)
        if form.is_valid():
            print "form is valid"
            user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data["password"])
            if user is not None:
                auth.login (request, user)
                print "The user is loggen in"
                try:
                    return HttpResponseRedirect("%shome_page/" % settings.SITE_URL)
                except:
                    return HttpResponseRedirect("%s" % settings.SITE_URL)        
            else:
                request.session['invalid_login'] = True
                request.session['logged_in'] = False
                errors=[]
                errors.append("Incorrect username and password combination!")
                return render_to_response('login.html', locals(),context_instance= global_context(request))
                 
        else:                       
            print "form not valid"
            invalid_login = session_get(request, "invalid_login")
            form = forms.LoginForm ()
            error_message = "The details provided by you do not match please try again"
    return render_to_response('login.html', locals(), context_instance= global_context(request))

