from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView , TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy  #is used in CBVs to redirect the users to a specific URL.
from .models import *
from api_floodmanagement.models import *
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
import pandas as pd
# Create your views here.
import folium

#{{ my_map|safe }}

from api_floodmanagement.tasks import *

class HomeListView(TemplateView):

    template_name = 'flood/home.html'

    def get_context_data(self, **kwargs):
       
        m = folium.Map([21.1458, 79.0882],width=750, height=500, zoom_start=20)
        folium.Marker([21.124181852903053, 79.00303866845013] , tooltip="click me" , popup="GHRIET").add_to(m)
        test = folium.Html('<b>Hello world</b>', script=True)

        popup = folium.Popup(test, max_width=2650)
        folium.RegularPolygonMarker(location=[51.5, -0.25], popup=popup).add_to(m)
        m=m._repr_html_() #updated
        
        
        image = CrowdSource.objects.all()
        context_old = super().get_context_data(**kwargs)
        context = { 'context_old':context_old , 'my_map': m , 'image':image}
        return context

class MapListView(TemplateView):
    

    template_name = 'flood/maplocation.html'

    def get_context_data(self, **kwargs):
       

        name = 'shantanu'
        data=CrowdSource.objects.all()
        context_old = super().get_context_data(**kwargs)
        context = {'name':name , 'context_old':context_old ,'x':data }
        return context

   


class PhotoCreateView(LoginRequiredMixin, CreateView):


    template_name = 'flood/create.html'
    fields = ['title']

    success_url = reverse_lazy('flood:home')  #Users will be redirected to the photo dashboard if the photo creation was successful.

    def post(self ,request):
        my_data = request.POST
        print(my_data)
        return super(CreateView, self).render_to_response()



    def form_valid(self, form):

        form.instance.submitter = self.request.user

        return super().form_valid(form)




class Help_list(ListView):
    model = UserHelpRequest

    context_object_name = 'userlist'
    template_name="webview/helpdesk.html"


def home1(request ):

    data=UserHelpRequest.objects.values_list('latitude' , 'longitude' )
    print(data)

    m = folium.Map([21.735362, 79.0882],width=750, height=500, zoom_start=20)
    for point in range(0, len(data)):
       
        folium.Marker(data[point], popup="GHRIET"  ,  icon=folium.Icon(color='Red', icon_color='white', icon='male', angle=0, prefix='fa') ).add_to(m)
    m=m._repr_html_() #updated
    context = {'my_map': m }
    return render(request,"flood/maplocation.html", context)


from geopy.geocoders import Nominatim
def dumptest(request):
    df = pd.read_html('https://aff.india-water.gov.in/table.php')
    tableDF = pd.DataFrame((df[1]))
    #run it only onces
    old_name = list(tableDF.keys())
    new_name = list(tableDF.iloc[0,:])
    new_name = ['Sno','Site_Name','River','State','District','Day1','Flood_Condition1','Max_WL1','Day2','Flood_Condition2','Max_WL2','Day3','Flood_Condition3','Max_WL3','Day4','Flood_Condition4','Max_WL4','Day5','Flood_Condition5','Max_WL5']
    renamed_dict = {}
    type(new_name[0])
    for i,j in zip(old_name,new_name):
        renamed_dict[i] =j

    updated_TableDF= tableDF.rename(columns=renamed_dict, inplace=False)
    Mapdata=updated_TableDF.iloc[1:,1:7]
    Location_data = Mapdata['District'].tolist()   #converting df column district to list
    # Initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")

    location_latitude = []  # empty list to append data
    location_longitude = []  # empty list to append data

    for i in Location_data:
        try:
            location = geolocator.geocode(i)
            #print(location.latitude)
            location_latitude.append(location.latitude)
            location_longitude.append(location.longitude)
        except:
            location_latitude.append("0.00")
            location_longitude.append("0.00")
            #print("error rised")
    Mapdata['latitude'] = location_latitude   #converting list to dataframe column
    Mapdata['longitude'] = location_longitude #converting list to dataframe column

    for Sit ,Riv,St, Dis,D1,FC1,lat,log in zip(Mapdata.Site_Name , Mapdata.River, Mapdata.State , Mapdata.District
     , Mapdata.Day1 , Mapdata.Flood_Condition1 , Mapdata.latitude , Mapdata.longitude):
        models = FloodForcastMap(Site_Name=Sit , River=Riv, State=St ,District=Dis , Day1=D1 ,Flood_Condition1=FC1 ,latitude=lat ,longitude=log)
        models.save()











    return  HttpResponse('Data Dumped Succcessfuly')






































def sendmain(request):
    send_mail_func.delay()
    return HttpResponse('SEND  MAIL')


import pandas as pd
def datadump(request):
    df = pd.read_html('https://aff.india-water.gov.in/table.php') #site Url from data we will fetch
    tableDF = pd.DataFrame((df[1]))
    #run it only onces
    old_name = list(tableDF.keys())
    new_name = list(tableDF.iloc[0,:])
    new_name = ['Sno','Site_Name','River','State','District','Day1','Flood_Condition1','Max_WL1','Day2','Flood_Condition2','Max_WL2','Day3','Flood_Condition3','Max_WL3','Day4','Flood_Condition4','Max_WL4','Day5','Flood_Condition5','Max_WL5']
    renamed_dict = {}
    type(new_name[0])
    for i,j in zip(old_name,new_name):
        renamed_dict[i] =j
    updated_TableDF= tableDF.rename(columns=renamed_dict, inplace=False)

    final=updated_TableDF.iloc[1:,1:]
    for Sit,Riv,St,Dis,D1,FC1,MW1,D2,FC2,MW2,D3,FC3,MW3,D4,FC4,MW4,D5,FC5,MW5 in zip(final.Site_Name , final.River, final.State , final.District , final.Day1 , final.Flood_Condition1 , 
    final.Max_WL1 , final.Day2 , final.Flood_Condition2 , final.Max_WL2 , final.Day3 , final.Flood_Condition3 ,
    final.Max_WL3 , final.Day4 ,final.Flood_Condition4 , final.Max_WL4 , final.Day5 , final.Flood_Condition5 , final.Max_WL5):
        models = ForcastData(Site_Name=Sit , River=Riv,State=St ,District=Dis , Day1=D1 ,Flood_Condition1=FC1 ,Max_WL1=MW1
                             ,Day2=D2 ,Flood_Condition2=FC2 ,Max_WL2=MW2 ,Day3=D3,Flood_Condition3=FC3 ,Max_WL3=MW3
                             ,Day4=D4 ,Flood_Condition4=FC4 ,Max_WL4=MW4 ,Day5=D5,Flood_Condition5=FC5 ,Max_WL5=MW5  )
        models.save()

    return HttpResponse('Data Dumped Succcessfuly')