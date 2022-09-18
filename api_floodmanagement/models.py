from dbm import dumb
import json
from pydoc import describe
from django.db import models
from django.dispatch import receiver
from api.models import User
from django.db.models.signals import pre_save

#django channels settings
from channels.layers import  get_channel_layer
from asgiref.sync import async_to_sync





# Create your models here.

REQUEST_STATUS=(
    ('HELP ALERT SEND TO AUTHORITIES' , 'HELP ALERT SEND TO AUTHORITIES'),
    ('HELP TO YOUR LOCATION DEPLOYED' , 'HELP TO YOUR LOCATION DEPLOYED'),
    ('OPERATION COMPLETED' , 'OPERATION COMPLETED'),
    )

EMERGENCY_TYPE=(
    ('Flood' , 'Flood'),
    ('Medical Help' , 'Medical Help'),
    ('Food and Shelter' , 'Food and Shelter'),
    )

CATEGORY=(
    ('Roads' , 'Roads'),
    ('Flood' , 'Flood'),
    ('Landslide' , 'Landslide'),
    ('Safehouse' , 'Safehouse'),
    
    )


class UserHelpRequest(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    latitude = models.DecimalField(max_digits=19, decimal_places=16)
    longitude = models.DecimalField(max_digits=19, decimal_places=16)
    TypeOfEmergency = models.CharField(max_length=30, choices = EMERGENCY_TYPE,default = 'Flood')
    RequestStatus = models.CharField(max_length = 30,choices = REQUEST_STATUS,default = 'HELP ALERT SEND TO AUTHORITIES')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    #def __str__(self):
        #return self.owner
    class Meta:
        ordering = ['created_at']


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    HelpRequest = models.ForeignKey(UserHelpRequest, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return "%s %s" % (self.owner, self.body )


class CrowdSource(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    longitude = models.DecimalField(max_digits=19, decimal_places=16)
    latitude = models.DecimalField(max_digits=19, decimal_places=16)
    category = models.CharField(max_length=30, choices = CATEGORY ,default = 'Flood')
    image = models.ImageField(upload_to='crowdsourcing/')
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    #def __str__(self):
        #return self.owner

    class Meta:
        ordering = ['created_at']

@receiver(pre_save , sender=CrowdSource)
def crowdsourcetask(sender , instance ,**kwargs):
    print("db updated")
    print(instance.owner)



class FloodForcastMap(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    Site_Name = models.CharField(max_length=20)
    River=models.CharField(max_length=20)
    State=models.CharField(max_length=20)
    District=models.CharField(max_length=20)
    Day1=models.CharField(max_length=20)
    Flood_Condition1=models.CharField(max_length=20)
    longitude = models.DecimalField(max_digits=19, decimal_places=16)
    latitude = models.DecimalField(max_digits=19, decimal_places=16)

    class Meta:
        ordering = ['created_at']



class ForcastData(models.Model):
    Site_Name=models.CharField(max_length=20)
    River=models.CharField(max_length=20)
    State=models.CharField(max_length=20)
    District=models.CharField(max_length=20)

    Day1=models.CharField(max_length=20)
    Flood_Condition1=models.CharField(max_length=20)
    Max_WL1=models.CharField(max_length=20)

    Day2=models.CharField(max_length=20)
    Flood_Condition2=models.CharField(max_length=20)
    Max_WL2=models.CharField(max_length=20)

    Day3=models.CharField(max_length=20)
    Flood_Condition3=models.CharField(max_length=20)
    Max_WL3=models.CharField(max_length=20)

    Day4=models.CharField(max_length=20)
    Flood_Condition4=models.CharField(max_length=20)
    Max_WL4=models.CharField(max_length=20)

    Day5=models.CharField(max_length=20)
    Flood_Condition5=models.CharField(max_length=20)
    Max_WL5=models.CharField(max_length=20)

   


class notification(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    notificationnn =  models.TextField(max_length=100)
    is_seen = models.BooleanField(default=False)


    def save(self , *args , **kwars):
        channel_layer = get_channel_layer()
        notification_objs = notification.objects.filter(is_seen=False)
        data={'currunt notification': self.notificationnn}

        async_to_sync(channel_layer.group_send)(
            'test_consumers_group' , {
                'type':'send_notification',
                'value':json.dumps(data)
            }
        )
        print('SAVE CALLED ')
        super(notification,self).save(*args , **kwars)
    

TIPS_CATEGORY=(
    ('All' , 'All'),
    ('Before Flood' , 'Before FLood'),
    ('During Flood' , 'During Flood'),
    ('After Flood' , 'After Flood'),
       )



class Tips(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    tips_category = models.CharField(max_length=30, choices = TIPS_CATEGORY ,default = 'All')
    image = models.ImageField(upload_to='tips/')




class FloodDataSet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    Site_Name = models.CharField(max_length=20)
    River=models.CharField(max_length=20)
    State=models.CharField(max_length=20)
    District=models.CharField(max_length=20)
    water_level = models.DecimalField(max_digits=10, decimal_places=5)
    longitude = models.DecimalField(max_digits=19, decimal_places=16)
    latitude = models.DecimalField(max_digits=19, decimal_places=16)

    class Meta:
        ordering = ['created_at']

class SaftyCheck(models.Model):
    longitude = models.DecimalField(max_digits=19, decimal_places=16)
    latitude = models.DecimalField(max_digits=19, decimal_places=16)



class Inunation(models.Model):
    latitude = models.DecimalField(max_digits=19, decimal_places=16)
    longitude = models.DecimalField(max_digits=19, decimal_places=16)
    water_level = models.DecimalField(max_digits=10, decimal_places=5)


class MsgBroadcast(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    msg =  models.TextField(max_length=100)
