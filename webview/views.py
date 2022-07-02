from django.shortcuts import render , HttpResponse, redirect
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.contrib import messages
from api.models import User
from api_floodmanagement.models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView , TemplateView

def Dashboard(request):
    if request.user.is_admin:
        user=User.objects.all()
        context = {'user':user}
        return render(request,"webview/dashboard.html" , context)
    else:
        return redirect(request,"webview/permission_error.html", context)
    return render(request,"webview/dashboard.html" , context)

def HelpDesk(request):

    help=UserHelpRequest.objects.all()
    context = {'help':help}

    return render(request,"webview/helpdesk.html" ,  context )
    
