#!/bin/bash
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Start app
>&2 echo "Postgres is up - executing command"

python manage.py migrate
python manage.py collectstatic --no-input
gunicorn personal_app.wsgi:application --bind 0.0.0.0:8000 --reload