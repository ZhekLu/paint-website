# pull official base image
FROM python:3.8-alpine

# set work directory
WORKDIR /paintweb

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /paintweb/entrypoint.sh
RUN chmod +x /paintweb/entrypoint.sh

# copy project
COPY . .

RUN echo "Collect static..."
RUN python manage.py collectstatic --noinput
RUN echo "Done."

EXPOSE $PORT

RUN rm /bin/sh && ln -s /bin/bash /bin/sh
# run entrypoint.sh
ENTRYPOINT ["/paintweb/entrypoint.sh"]