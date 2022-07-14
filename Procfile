 web: gunicorn configurations.wsgi --log-file -
celery: celery -A configurations(project name) worker --pool=solo -l info     
celerybeat: celery -A configurations beat --loglevel=info 
