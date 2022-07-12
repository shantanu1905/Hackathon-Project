
from celery  import shared_task
from django.conf import settings
from api.models import User
from configurations import settings
from django.core.mail import send_mail
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

