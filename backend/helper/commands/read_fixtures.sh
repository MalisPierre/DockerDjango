echo $'\n'
echo $'LOADING AUTH MODULE ...'
python manage.py loaddata core/fixtures/permission.json
python manage.py loaddata core/fixtures/user.json
echo $'\n'
echo $'LOADING CINEMA MODULE ...'
python manage.py loaddata core/fixtures/filmcateg.json
python manage.py loaddata core/fixtures/film.json
echo $'\n'