from django.contrib import admin
from django.urls import path 
from .views import *

app_name = 'flood'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeListView.as_view(), name='home'),
  
   
       
       
    path('helpmap',  HelpMap, name='HelpMap'),
    path('crowdsourcemap',  CrowdSourceMap, name='CrowdSourceMap'),
    path('crowdsourcelist',  Crowdsource_list.as_view(), name='Crowdsourcelist'),

    path('route',  routefinder, name='routefinder'),






    
]