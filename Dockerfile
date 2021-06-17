# Python and Linux Version
FROM python:3.9-slim-buster

COPY requirements.txt /app/requirements.txt

# Configure server
RUN set -ex \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r app/requirements.txt

# Switch directory
WORKDIR /app

ADD . .

# DEV ENVIRONMENT
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

# GUNICORN IN DEV ENVIRONMENT
#EXPOSE 8000
#CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "core.wsgi:application"]

# HEROKU DEPLOYMENT
CMD gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
