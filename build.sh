#!/usr/bin/env bash

set -o errexit  # exit on error

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

if [ -n $CREATE_SUPERUSER ];
then
  python manage.py createsuperuser --phone --no-input
fi
