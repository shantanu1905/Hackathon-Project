from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView , TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import *
from api_floodmanagement.models import *
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
import pandas as pd
# Create your views here.
from django.contrib.auth.models import User
from folium.plugins import *
import folium
#{{ my_map|safe }}
from api_floodmanagement.tasks import *
import openrouteservice
from openrouteservice import convert
import json

#Home Screen
class HomeListView(TemplateView):
    template_name = 'flood/home.html'

#Admin Screen for Crowdsource data
def Crowdsource_list(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            object_list = CrowdSource.objects.all()
            context = {
                'object_list': object_list,
                }
            return render(request , "flood/crowdsourcelist.html" , context)
        messages.warning(request, 'To view this page Admin Permission is required !!')
        return render(request,"flood/home.html")
    else:
        messages.warning(request, 'To view this page login is required !!')
        return render(request,"flood/home.html")

#Admin delete function for Crowdsource data
def deletecs(request , CrowdSource_id):
    item= CrowdSource.objects.get(pk=CrowdSource_id)
    item.delete()
    messages.success(request, 'Deleted Successfullly')
    return render(request , "flood/crowdsourcelist.html")


#Admin Screen for Help data
def HelpRequest_list(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            object_list = UserHelpRequest.objects.all()
            context = {
                'object_list': object_list,
                }
            return render(request , "flood/Userhelplist.html" , context)
        messages.warning(request, 'To view this page Admin Permission is required !!')
        return render(request,"flood/home.html")
    else:
        messages.warning(request, 'To view this page login is required !!')
        return render(request,"flood/home.html")

#Admin delete function for Help data
def deletehr(request , UserHelpRequest_id):
    item= UserHelpRequest.objects.get(pk=UserHelpRequest_id)
    item.delete()
    messages.success(request, 'Deleted Successfullly')
    return render(request , "flood/Userhelplist.html")

#Update function for Help data
def update(request, UserHelpRequest_id):
  Helpdata = UserHelpRequest.objects.get(pk=UserHelpRequest_id)
  context = {
    'Helpdata': Helpdata,
  }
  return render(request , "flood/update.html" , context)

#Update function for Help data
def updaterecord(request, UserHelpRequest_id):
  RequestStatus = request.POST['RequestStatus']

  Helpdata = UserHelpRequest.objects.get(pk=UserHelpRequest_id)
  Helpdata.RequestStatus = RequestStatus
  Helpdata.save()
  messages.success(request, 'Request Updated Successfullly')
  return render(request , "flood/Userhelplist.html")
  
#Help Request Map 
def HelpMap(request ):
    if request.user.is_authenticated:
        if request.user.is_admin:
            data=UserHelpRequest.objects.values_list('latitude' , 'longitude' )
    

            df = pd.DataFrame(list(UserHelpRequest.objects.all().values()))
            #print(df)
            locations = df[['latitude', 'longitude']]
            locationlist = locations.values.tolist()
        
            m = folium.Map([20.5937, 78.9629], zoom_start=12)
            for point in range(0, len(locationlist)):
                folium.Marker(locationlist[point], popup='created_at:  '+str(df['created_at'][point])+' \n'+ 'TypeOfEmergency:  ' 
                +str(df['TypeOfEmergency'][point]) + '\n' + 'RequestStatus' + str(df['RequestStatus'][point]),).add_to(m)
        
             
            m=m._repr_html_() #updated
            context = {'my_map': m }
            return render(request,"flood/helpmap.html", context)
        messages.warning(request, 'To view this page Admin Permission is required !!')
        return render(request,"flood/home.html")
    else:
        messages.warning(request, 'To view this page login is required !!')
        return render(request,"flood/home.html")

#CrowdSource data Map
def CrowdSourceMap(request ):
    if request.user.is_authenticated:
        if request.user.is_admin:
            df = pd.DataFrame(list(CrowdSource.objects.all().values()))
            #print(df)
            locations = df[['latitude', 'longitude']]
            locationlist = locations.values.tolist()         
            m = folium.Map([20.5937, 78.9629], zoom_start=12)
            for point in range(0, len(locationlist)):
                folium.Marker(locationlist[point], popup='created_at:  '+str(df['created_at'][point])+' \n'+ 'description:  ' 
                +str(df['description'][point]) + '\n' + 'category' + str(df['category'][point]),).add_to(m)         
             
            m=m._repr_html_() #updated
            context = {'my_map': m }
            return render(request,"flood/crowdsourcemap.html", context)
        messages.warning(request, 'To view this page Admin Permission is required !!')
        return render(request,"flood/home.html")
    else:
        messages.warning(request, 'To view this page login is required !!')
        return render(request,"flood/home.html")


def routefinder(request):
    client = openrouteservice.Client(key='5b3ce3597851110001cf6248ad84107cc5eb4c1cbf77a7cea0874772')
    coords = ((21.1146138,79.1003920024),(21.06201943,78.8702031303))
    res = client.directions(coords)
    geometry = client.directions(coords)['routes'][0]['geometry']
    decoded = convert.decode_polyline(geometry)
    
    distance_txt = "<h4> <b>Distance :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['distance']/1000,1))+" Km </strong>" +"</h4></b>"
    duration_txt = "<h4> <b>Duration :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['duration']/60,1))+" Mins. </strong>" +"</h4></b>"

    m = folium.Map(location=[6.074834613830474, 80.25749815575348],zoom_start=10, control_scale=True,tiles="cartodbpositron")
    folium.GeoJson(decoded).add_child(folium.Popup(distance_txt+duration_txt,max_width=300)).add_to(m)
    
    #source marker
    folium.Marker(location=list(coords[0][::-1]),popup="Galle fort",icon=folium.Icon(color="green"),).add_to(m)
    #destination marker
    folium.Marker(location=list(coords[1][::-1]),popup="Jungle beach",icon=folium.Icon(color="red"),).add_to(m)
    m.save('map.html')

    m=m._repr_html_() #updated

    context = {'my_map': m }


    return render(request,"flood/helpmap.html",context)





#Update function for MsgBroadcast data
def msgupdate(request, msg_id=1):
  msgdata = MsgBroadcast.objects.get(pk=msg_id)
  context = {
    'msgdata': msgdata,
  }
  return render(request , "flood/msgupdate.html" , context)

#Update function for MsgBroadcast data
def msgupdatepage(request, msg_id):
  msgstatus = request.POST['msgstatus']

  msgdata = MsgBroadcast.objects.get(pk=msg_id)
  msgdata.msg = msgstatus
  msgdata.save()
  messages.success(request, 'Msg Updated Successfullly')
  return render(request , "flood/msgpage.html")
  

def msgpage(request):
  msgdata = MsgBroadcast.objects.get(pk=1)
  context = {
    'msgdata': msgdata,
  }
  return render(request , "flood/msgpage.html" , context)




















