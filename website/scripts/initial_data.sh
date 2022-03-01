#!/usr/bin/env bash

echo "- Create demo data"
python3 website/manage.py migrate

cp initial_migrations/base/0002_initial_data.py website/base/migrations
cp initial_migrations/usermanager/0002_initial_data.py website/usermanager/migrations

python3 website/manage.py collectstatic