#!/usr/bin/env bash
# Useful only in staging on local machine.
echo "Start backup"
echo "NOTE: use only in staging!!"

# Usermanager
echo "- restore data for Usermanager"
poetry run python3 ../website/manage.py loaddata ../website/fixtures/usermanager/userprofile.json

# Standard Apps
echo "- restore data for Django's standard apps"
poetry run python3 ../website/manage.py loaddata ../website/fixtures/sites.json

# Base
echo "- restore data for Base"
poetry run python3 ../website/manage.py loaddata ../website/fixtures/base/fileupload.json
poetry run python3 ../website/manage.py loaddata ../website/fixtures/base/sharedcategories.json
poetry run python3 ../website/manage.py loaddata ../website/fixtures/base/sitesocialurls.json
poetry run python3 ../website/manage.py loaddata ../website/fixtures/base/siteurls.json
poetry run python3 ../website/manage.py loaddata ../website/fixtures/base/sitecustomization.json
poetry run python3 ../website/manage.py loaddata ../website/fixtures/base/organogram.json

# GisManager
echo "- restore data for GisManager"
poetry run python3 ../website/manage.py loaddata ../website/fixtures/gismanager/geoserverurl.json
poetry run python3 ../website/manage.py loaddata ../website/fixtures/gismanager/ogclayer.json
poetry run python3 ../website/manage.py loaddata ../website/fixtures/gismanager/basemapprovider.json
poetry run python3 ../website/manage.py loaddata ../website/fixtures/gismanager/basemap.json
poetry run python3 ../website/manage.py loaddata ../website/fixtures/gismanager/webgisproject.json

echo "End process"