# Team-Ghostpye
# Smart India Hackathon 2022
![SIH2022](https://user-images.githubusercontent.com/55245862/156772177-691163b0-a0b0-4102-a945-37b4f281e4c4.jpeg)



## Problem Statement Code: 
> #### RK1111 (Central Water Commission (CWC), Ministry of Jal Shakti)
> Two-way mobile communication (G2C and C2G) for dissemination of flood forecasts to end users and collection of real time data of inundation area through crowd sourcing. <br>
> #### Detailed Problem Statement
> Web-based system for dissemination of flood forecasts was operationalized by CWC in 2014 with information being made available on near real time basis (Ref: https://ffs.tamcnhp.com/). In addition to this, CWC has partnered with Google to disseminate the flood warning through its Public Alert platform. An additional channel to reach out to the end beneficiaries is through deployment of real time messaging service of flood forecasts soon after their generation with opt-in option for end users as well as provision for blanket area specific messaging in affected areas. End beneficiaries can in turn help in crowd sourcing of information related to inundation with geo tagged as well as time stamped images and information related to water levels. Such crowd sourced data can help in ground truthing of inundation for known events of floods which will enable in future endeavours of generation of flood inundation forecasts and flood plain zonation.


## Features

1. Login/Sign Up.
2. JWT Authentication.
3. Multiuser Authentication (User and Admin).
4. Admin Panel Support (View,Update,Delete Data)
5. User can request for help in case he/she is stuck in the floods.
6. Flood forcasting :Flood warnings, alerts are send to user before acctual flood come to their location.
7. User Crowdsourcing of flood data.(with the help of crowdsourcing the government can actually understand current status of flood affected area.)
8. SOS (At time of Emergency, User can share their live location to their family,friends via sms service without INTERNET/OFFLINE. )
9. Live Weather
10. Message broadcasting G2C(Government to Consumers)
11. User can view other informations like *Do and Don't , Emergency Helpline Numbers*

## Technology Stack to be used:

<img src="https://img.shields.io/badge/html5%20-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white"/>  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/> <img src="https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white"/>   <img src="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white"/>    <img src="https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens"/>    <img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white"/>   <img src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray"/>  <img src="https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white"/>   <img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white"/>   <img src="https://img.shields.io/badge/javascript%20-%23323330.svg?&style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/>  <img src="https://img.shields.io/badge/markdown-%23000000.svg?&style=for-the-badge&logo=markdown&logoColor=white"/>  <img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"/> 

## Technology Stack:
- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Django, Django Rest Framework
- **IDE**: VS Code
- **Design**: Figma, Canva
- **API Testing & Documentation**: Postman
- **Version Control**: Git and GitHub
- **Programming Languages**: Python
- **Database**: SQLite
- **Hosting**: Heroku


### How to Get Started?

#### GitHub Repository Structure


| S.No. | Branch Name                                                                             | Purpose                       |
| ----- | --------------------------------------------------------------------------------------- | ----------------------------- |
| 1.    | [master](https://github.com/shantanu1905/Hackathon-Project/tree/master)                 | contains all backend code     |
| 1.    | [master]()                                                                              | contains all Frontend code    |


### Backend Setup Instructions

- Fork and Clone the repo using
```
 git clone https://github.com/shantanu1905/Hackathon-Project.git
```
- Install the Dependencies from `requirements.txt`
- Make sure your system has python installed and before installing dependencies make sure your virtual environment is activated .
```
 pip install -r requirements.txt 
```
- Run the Server and see the demo at [http://localhost:8000/](http://localhost:8000/)
```
 python manage.py runserver
```
- Celery Server Commands(required Backend Service need to run for proper functioning of application).
- Make sure Redis is installed and Redis server is running 
- Celery Worker command
```
 celery -A configurations worker --pool=solo -l info
```
- Celery Beat command
```
celery -A configurations beat --loglevel=info <br>
```

#### All things are done and you are good to go


