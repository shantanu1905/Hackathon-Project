echo " BUILD START"
python3.7.12 -m pip install -r requirements.txt
python3.7.12 manage.py collectstatic --noinput --clear
echo " BUILD STOP"