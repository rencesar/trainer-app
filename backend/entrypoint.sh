#!/bin/bash
echo "Waiting for postgres..."
while ! nc -z db 5432 ; do
  sleep 0.1
done
echo "PostgreSQL started"

python manage.py migrate
python manage.py collectstatic --no-input
gunicorn settings.wsgi:application --bind 0.0.0.0:8000 --reload