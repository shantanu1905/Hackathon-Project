from django.contrib import admin
from django.urls import path 
from .views import *

app_name = 'webview'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Dashboard , name='Dashboard'),
   



]