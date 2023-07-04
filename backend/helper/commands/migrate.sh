echo $'\n'
echo $'MIGRATING ...'
python manage.py makemigrations
python manage.py migrate
echo $'\n'