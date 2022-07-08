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
    list_display = ('owner' , 'created_at' )

admin.site.register(CrowdSource , CrowdSourceOptions)