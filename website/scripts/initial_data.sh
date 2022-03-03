#!/usr/bin/env bash

echo "- Create demo data"
python3 website/manage.py makemigrations

cp initial_migrations/base/0002_initial_data.py website/base/migrations
cp initial_migrations/usermanager/0002_initial_data.py website/usermanager/migrations

python3 website/manage.py migrate

python3 website/manage.py collectstatic --noinput