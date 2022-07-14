from celery  import shared_task
from django.conf import settings
from api.models import User
from configurations import settings
from django.core.mail import send_mail
from api_floodmanagement.models import *
import pandas as pd
from configurations.celery import *

@shared_task(bind=True)

# Given below is a simple example of Celery Worker 
# This means it simply performs task when particular URL is hit 


def send_mail_func(self):
    users=User.objects.all()
    for user in users:
        mail_subject = "Celery Testing"
        message="test mail"
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email= settings.EMAIL_HOST_USER , 
            recipient_list=[to_email],
            fail_silently=True # if one mail is not send then it won't affect others 
        )

    return "done"


@app.task(bind=True)
def datadump_task(self):
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

    return 'Data Dumped Succcessfuly'



@app.task(bind=True)
def cleanup_task(self):
    ForcastData.objects.all().delete()
    return 'done task'
