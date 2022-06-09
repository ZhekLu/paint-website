#!/bin/sh

#if [ "$DATABASE" = "postgres" ]
#then
#    echo "Waiting for postgres..."
#
#    while ! nc -z "$SQL_HOST" "$SQL_PORT"; do
#      sleep 0.1
#    done
#
#    echo "PostgreSQL started."
#fi

echo "Collect static..."
python manage.py collectstatic --noinput
echo "Done."

#python manage.py flush --no-input
python manage.py makemigrations --no-input
python manage.py migrate

python manage.py runserver 0.0.0.0:8000

exec "$@"

