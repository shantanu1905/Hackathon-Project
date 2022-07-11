from django.urls import path , include
from api_floodmanagement.views import *

urlpatterns = [
path('help/' , HelpList.as_view()  , name ='help' ) ,                      #to view userhelp request
path('helpdetails/<int:pk>/', HelpDetail.as_view() , name='HelpDetails'),      #to view userhelp details/update/delete
path('crowdsource/' , CrowdSource.as_view()  , name ='CrowdSource' ) ,       #To view/post crowdsource data
path('crowdsourcedetails/<int:pk>/', CrowdSourceDetails.as_view() , name='CrowdSourceDetails'),      #to view userhelp details/update/delete


]
