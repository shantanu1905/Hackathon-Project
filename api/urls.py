from django.urls import path , include
from api.views import *

urlpatterns = [
    path('register/' , UserRegistrationView.as_view()  , name ='register' ) ,
    path('login/' , UserLoginView.as_view()  , name ='login' ) ,
    path('profile/' , UserProfileView.as_view()  , name ='profile' ) ,
    path('send-reset-password-email/' , SendPasswordResetEmailView.as_view()  , name ='send-reset-password-email' ) ,




    

]
