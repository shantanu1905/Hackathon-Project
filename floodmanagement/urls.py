from django.contrib import admin
from django.urls import path 
from .views import *

app_name = 'flood'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeListView.as_view(), name='home'),
  
   
       
       
    path('helpmap',  HelpMap, name='HelpMap'),
    path('crowdsourcemap',  CrowdSourceMap, name='CrowdSourceMap'),
    path('crowdsourcelist',  Crowdsource_list, name='Crowdsourcelist'),
    path('deletecs/<int:CrowdSource_id>/' ,deletecs, name='deletecs'),
    path('helplist',  HelpRequest_list, name='HelpRequest_list'),
    path('deletehr/<int:UserHelpRequest_id>/' ,deletehr, name='deletehr'),
    path('update/<int:UserHelpRequest_id>', update, name='update'),
    path('update/updaterecord/<int:UserHelpRequest_id>', updaterecord, name='updaterecord'),

    path('route',  routefinder, name='routefinder'),

]





    
