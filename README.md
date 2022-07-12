# Hackathon-Project

### steps to install project <br>
1. clone github repo
2. create virtual environment 
3. activate virtual environment 
4. then open cmd and type **pip install -r requirements.txt**
5. python manage.py runserver **(to run our server)**

### Celery Server cmd

Celery Worker on windows <br>
celery -A configurations(project name) worker --pool=solo -l info     <br>

Celery Beat <br>
celery -A configurations beat --loglevel=info <br>

