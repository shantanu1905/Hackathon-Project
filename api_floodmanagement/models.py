from django.db import models
from django.forms import JSONField
from api.models import User


# Create your models here.

REQUEST_STATUS=(
    ('HELP ALERT SEND TO AUTHORITIES' , 'HELP ALERT SEND TO AUTHORITIES'),
    ('HELP REQUEST RECIEVED ' , 'HELP ALERT SEND TO AUTHORITIES'),
    ('HELP TO YOUR LOCATION DEPLOYED' , 'HELP TO YOUR LOCATION DEPLOYED'),
    ('OPERATION COMPLETED' , 'OPERATION COMPLETED'),

)

EMERGENCY_TYPE=(
    ('Flood' , 'Flood'),
    ('Highway Safety' , 'Highway Safety'),
    ('Landslide' , 'Landslide'),
    ('Power Outage' , 'Power Outage'),
    ('Medical Help' , 'Medical Help'),
    ('Food' , 'Food'),
)



class UserHelpRequest(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    latitude = models.DecimalField(max_digits=19, decimal_places=16)
    longitude = models.DecimalField(max_digits=19, decimal_places=16)
    TypeOfEmergency = models.CharField(max_length=30, choices = EMERGENCY_TYPE,default = '0')
    RequestStatus = models.CharField(max_length = 30,choices = REQUEST_STATUS,default = 'HELP ALERT SEND TO AUTHORITIES')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s %s" % (self.owner, self.TypeOfEmergency )
    class Meta:
        ordering = ['created']


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    HelpRequest = models.ForeignKey(UserHelpRequest, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return "%s %s" % (self.owner, self.body )