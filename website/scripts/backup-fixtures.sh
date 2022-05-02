#!/usr/bin/env bash
echo "Start backup"

# Standard Apps
echo "- make fixtures for Django's standard apps"
python3 ./website/manage.py dumpdata sites --indent 2 > ./website/fixtures/sites.json

# Base
echo "- make fixtures for Base"
python3 ./website/manage.py dumpdata base.sitesocialurls --indent 2 > ./website/fixtures/base/sitesocialurls.json
python3 ./website/manage.py dumpdata base.siteurls --indent 2 > ./website/fixtures/base/siteurls.json
python3 ./website/manage.py dumpdata base.sitecustomization --indent 2 > ./website/fixtures/base/sitecustomization.json

# Usermanager
echo "- make fixtures for Usermanager"
python3 ./website/manage.py dumpdata usermanager.userprofile --indent 2 > ./website/fixtures/usermanager/userprofile.json

echo "End process"