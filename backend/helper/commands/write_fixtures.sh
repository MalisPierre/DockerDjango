echo $'\n'
echo $'WRITTING AUTH MODULE ...'
python manage.py dumpdata auth.permission --indent 4 > core/fixtures/permission.json
python manage.py dumpdata auth.user --indent 4 > core/fixtures/user.json
echo $'\n'
echo $'WRITTING CINEMA MODULE ...'
python manage.py dumpdata cinema.filmcateg --indent 4 > core/fixtures/filmcateg.json
python manage.py dumpdata cinema.film --indent 4 > core/fixtures/film.json
echo $'\n'