#!/usr/bin/env bash
# Useful only in development on local machine.
echo "Start backup"

# Usermanager
echo "- make fixtures for Usermanager"
python3 ./website/manage.py loaddata ./website/fixtures/usermanager/userprofile.json

# Standard Apps
echo "- make fixtures for Django's standard apps"
python3 ./website/manage.py loaddata ./website/fixtures/sites.json

# Base
echo "- make fixtures for Base"
python3 ./website/manage.py loaddata ./website/fixtures/base/fileupload.json
python3 ./website/manage.py loaddata ./website/fixtures/base/sharedcategories.json
python3 ./website/manage.py loaddata ./website/fixtures/base/sitesocialurls.json
python3 ./website/manage.py loaddata ./website/fixtures/base/siteurls.json
python3 ./website/manage.py loaddata ./website/fixtures/base/sitecustomization.json

echo "End process"