#!/usr/bin/env bash

echo "- Build DB tables"
python3 website/manage.py makemigrations
python3 website/manage.py migrate
echo "- Collect static files"
python3 website/manage.py collectstatic --noinput