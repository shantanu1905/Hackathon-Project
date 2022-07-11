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