from django.urls import path , include
from api_floodmanagement.views import *

urlpatterns = [
path('help/' , HelpList.as_view()  , name ='register' ) ,
path('helpdetails/<int:pk>/', HelpDetail.as_view() , name='HelpDetails'),

]
