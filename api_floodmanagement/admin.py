from django.contrib import admin
from api_floodmanagement.models import *
from django.utils.html import format_html

# Register your models here.

class Help(admin.ModelAdmin):
    list_display = ('owner' , 'TypeOfEmergency','RequestStatus' , 'created_at' , 'Details')
    list_filter = ('created_at' , 'updated_at')

    def Details(self , obj):
        return format_html(f'<a href = "/admin/api_floodmanagement/userhelprequest/{obj.id}/change/" class="default"> View </a>')

admin.site.register(UserHelpRequest , Help)
admin.site.register(Comment)


class CrowdSourceOptions(admin.ModelAdmin):
    list_display = ('owner' , 'category' , 'image' , 'created_at' , 'photo_tag' , 'Details' )
    readonly_fields = ('photo_tag' , )

    def photo_tag(self , obj):
        return format_html(f'<img scr="/media/crowdsourcing/{obj.image}" class="img-responsive" style="width: 100px; hight: "/>')

    def Details(self , obj):
        return format_html(f'<a href = "/admin/api_floodmanagement/crowdsource/{obj.id}/change/" class="default"> View </a>')

    def map_tag(self , obj):
        return format_html(f'''
        
        <h1>shan<h1>
        
        
        ''')


admin.site.register(CrowdSource , CrowdSourceOptions)



class ForcastOptions(admin.ModelAdmin):
    list_display = ('Site_Name' , 'River' , 'State' , 'District' , 'Details')


    def Details(self , obj):
        return format_html(f'<a href = "/admin/api_floodmanagement/forcastdata/{obj.id}/change/" class="default"> View </a>')

admin.site.register(ForcastData , ForcastOptions)