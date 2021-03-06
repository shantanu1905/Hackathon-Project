from django.contrib import admin
from django.urls import path 
from .views import *

app_name = 'flood'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeListView.as_view(), name='home'),
    path('create', PhotoCreateView.as_view(), name='create'),
    path('helplist/', Help_list.as_view(), name='helplist'),
    path('mapview/',  MapListView.as_view(), name='mapview'),
    path('mail/',  sendmain, name='sendmail'),
    path('dump/',  datadump, name='datadump'),




     path('delete/<int:UserHelpRequest_id>/' ,delete, name='delete'),
    
]