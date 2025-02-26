APP=mysql
python manage.py makemigrations $APP
python manage.py migrate --database=$APP
python manage.py loaddata fixtures/$APP.json --app $APP --database $APP

APP=pgsql
python manage.py makemigrations $APP
python manage.py migrate --database=$APP
python manage.py loaddata fixtures/$APP.json --app $APP --database $APP

APP=sqlite
python manage.py makemigrations $APP
python manage.py migrate --database=default
python manage.py loaddata fixtures/$APP.json --app $APP --database default

# Start Django
python manage.py runserver 0.0.0.0:8000