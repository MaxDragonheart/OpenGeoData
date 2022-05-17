#!/usr/bin/env bash
# Useful only in development on local machine.
echo "Start backup"
echo "NOTE: use only in staging!!"

# Standard Apps
echo "- make fixtures for Django's standard apps"
poetry run python3 ../website/manage.py dumpdata sites --indent 2 > ../website/fixtures/sites.json

# Base
echo "- make fixtures for Base"
poetry run python3 ../website/manage.py dumpdata base.fileupload --indent 2 > ../website/fixtures/base/fileupload.json
poetry run python3 ../website/manage.py dumpdata base.sharedcategories --indent 2 > ../website/fixtures/base/sharedcategories.json
poetry run python3 ../website/manage.py dumpdata base.sitesocialurls --indent 2 > ../website/fixtures/base/sitesocialurls.json
poetry run python3 ../website/manage.py dumpdata base.siteurls --indent 2 > ../website/fixtures/base/siteurls.json
poetry run python3 ../website/manage.py dumpdata base.sitecustomization --indent 2 > ../website/fixtures/base/sitecustomization.json
poetry run python3 ../website/manage.py dumpdata base.organogram --indent 2 > ../website/fixtures/base/organogram.json

# GisManager
echo "- make fixtures for GisManager"
poetry run python3 ../website/manage.py dumpdata gismanager.geoserverurl --indent 2 > ../website/fixtures/gismanager/geoserverurl.json
poetry run python3 ../website/manage.py dumpdata gismanager.ogclayer --indent 2 > ../website/fixtures/gismanager/ogclayer.json
poetry run python3 ../website/manage.py dumpdata gismanager.basemapprovider --indent 2 > ../website/fixtures/gismanager/basemapprovider.json
poetry run python3 ../website/manage.py dumpdata gismanager.basemap --indent 2 > ../website/fixtures/gismanager/basemap.json
poetry run python3 ../website/manage.py dumpdata gismanager.webgisproject --indent 2 > ../website/fixtures/gismanager/webgisproject.json

# Usermanager
echo "- make fixtures for Usermanager"
poetry run python3 ../website/manage.py dumpdata usermanager.userprofile --indent 2 > ../website/fixtures/usermanager/userprofile.json

echo "End process"