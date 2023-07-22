#!/bin/bash

set -e

# DB_HOST=${POSTGRES_HOST}
# DB_PORT=${POSTGRES_PORT}

# Ожидание подключения Redis
# >&2 echo "Redis host: ${REDIS_HOST}"
# >&2 echo "Redis port: ${REDIS_PORT}"

# while ! timeout 1 bash -c "</dev/tcp/${REDIS_HOST}/${REDIS_PORT}" &>/dev/null; do
#     echo "Redis service is unavailable - sleeping"
#     sleep 1;
# done;

# >&2 echo "Redis is up - executing command"

# # Ожидание подключения PostgreSQL
# >&2 echo "Postgres-server host: ${DB_HOST}"
# >&2 echo "Postgres-server port: ${DB_PORT}"

# while ! timeout 1 bash -c "</dev/tcp/${DB_HOST}/${DB_PORT}" &>/dev/null; do
#     echo "Postgres service is unavailable - sleeping"
#     sleep 1;
# done;

# >&2 echo "Postgres is up - executing command"

python3 manage.py migrate
python3 manage.py collectstatic --noinput

# if [ $DJANGO_SUPERUSER_USERNAME ]
# then
#     python3 manage.py createsuperuser \
#     --noinput \
#     --username $DJANGO_SUPERUSER_USERNAME \
#     --email $DJANGO_SUPERUSER_EMAIL
# fi

# supervisord
# gunicorn --workers 3 --bind 0.0.0.0:8000 config.wsgi:application
python3 manage.py runserver 0.0.0.0:8000