from django.urls import path , include
from api_floodmanagement.views import *

urlpatterns = [
path('help/' , HelpList.as_view()  , name ='help' ) ,                      #to view userhelp request
path('helplist/' , HelpAllList.as_view()  , name ='help' ) ,                   #To Get userhelp request data for only login user
path('helpdetails/<int:pk>/', HelpDetail.as_view() , name='HelpDetails'),      #to view userhelp details/update/delete
path('crowdsource/' , CrowdSourceList.as_view()  , name ='CrowdSource' ) ,       #To view/post crowdsource data
path('crowdsourcedetails/<int:pk>/', CrowdSourceDetails.as_view() , name='CrowdSourceDetails'),      #to view userhelp details/update/delete
path('crowdsourcelist/' , CrowdSourceListView.as_view()  , name ='CrowdSourceList' ) ,
path('forcast/', ForcastList.as_view() , name='ForcastData'),      #to GET Forcast Data
path('forcastmap/', ForcastMapList.as_view() , name='ForcastMap'),      #to GET Forcast Data for Map plotting
path('tips/', Tips.as_view() , name='Tips'),      #to GET Tips Data for Do's and Don'ts
path('saftycheck/', saftycheck.as_view() , name='saftycheck'),      #to GET Tips Data for Do's and Don'ts
path('test/', calculatedistance , name='calculatedistance'),      #to GET Tips Data for Do's and Don'ts
path('inundation/' , Inundation.as_view() ,  name='Inundation'),
path('broadcast/' , MsgBroadcast.as_view() ,  name='MsgBroadcast'),    











]
