#!/bin/sh

set -e

if [ "$1" = 'uwsgi' ]; then
    python django-jewels/manage.py collectstatic --noinput
    python django-jewels/manage.py migrate

    exec uwsgi uwsgi.ini
fi

exec "$@"
