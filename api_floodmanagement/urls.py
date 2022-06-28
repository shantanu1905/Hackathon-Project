from django.urls import path , include
from api_floodmanagement.views import *

urlpatterns = [
    path('forcastday1/' , ForcastData , name ='forcast' ) ,
  

    

]
