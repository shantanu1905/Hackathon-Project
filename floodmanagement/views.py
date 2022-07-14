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


def delete(request , UserHelpRequest_id):
    item= UserHelpRequest.objects.get(pk=UserHelpRequest_id)
    item.delete()
    messages.success(request, 'User Request is Deleted')
    return render(request , "flood/deleted_successfully.html")

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