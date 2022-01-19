#!/bin/bash

python manage.py migrate
python manage.py collectstatic --noinput
exec gunicorn Telegram_newsletter.wsgi:application -b 0.0.0.0:8000 --reload


