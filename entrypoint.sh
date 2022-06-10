#!/bin/sh

RUN echo "Collect static..."
RUN python manage.py collectstatic --noinput
RUN echo "Done."

#python manage.py flush --no-input
python manage.py makemigrations --no-input
python manage.py migrate --no-input

python manage.py runserver 0.0.0.0:$PORT

exec "$@"

