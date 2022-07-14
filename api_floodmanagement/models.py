from django.db import models
from api.models import User

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




CATEGORY=(
    ('Roads' , 'Roads'),
    ('Flood' , 'Flood'),
    ('Landslide' , 'Landslide'),
    ('Safehouse' , 'Safehouse'),
    
    )

class CrowdSource(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    longitude = models.DecimalField(max_digits=19, decimal_places=16)
    latitude = models.DecimalField(max_digits=19, decimal_places=16)
    category = models.CharField(max_length=30, choices = CATEGORY ,default = 'Flood')
    image = models.ImageField(upload_to='crowdsourcing/')

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    #def __str__(self):
        #return self.owner

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

   


    



    