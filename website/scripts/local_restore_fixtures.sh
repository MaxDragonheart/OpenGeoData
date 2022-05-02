#!/usr/bin/env bash
# Useful only in development on local machine.
echo "Start backup"
echo "NOTE: use only in development!!"

# Usermanager
echo "- restore data for Usermanager"
python3 ../website/manage.py loaddata ../website/fixtures/usermanager/userprofile.json

# Standard Apps
echo "- restore data for Django's standard apps"
python3 ../website/manage.py loaddata ../website/fixtures/sites.json

# Base
echo "- restore data for Base"
python3 ../website/manage.py loaddata ../website/fixtures/base/fileupload.json
python3 ../website/manage.py loaddata ../website/fixtures/base/sharedcategories.json
python3 ../website/manage.py loaddata ../website/fixtures/base/sitesocialurls.json
python3 ../website/manage.py loaddata ../website/fixtures/base/siteurls.json
python3 ../website/manage.py loaddata ../website/fixtures/base/sitecustomization.json

# GisManager
echo "- restore data for GisManager"
python3 ../website/manage.py loaddata ../website/fixtures/gismanager/geoserverurl.json
python3 ../website/manage.py loaddata ../website/fixtures/gismanager/ogclayer.json
python3 ../website/manage.py loaddata ../website/fixtures/gismanager/basemapprovider.json
python3 ../website/manage.py loaddata ../website/fixtures/gismanager/basemap.json
python3 ../website/manage.py loaddata ../website/fixtures/gismanager/webgisproject.json

echo "End process"