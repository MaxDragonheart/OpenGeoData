#!/usr/bin/env bash
echo "Start backup"

# Standard Apps
echo "- make fixtures for Django's standard apps"
python3 ./website/manage.py dumpdata sites --indent 2 > ./website/fixtures/sites.json

# Base
echo "- make fixtures for Base"
python3 ./website/manage.py dumpdata base.fileupload --indent 2 > ./website/fixtures/base/fileupload.json
python3 ./website/manage.py dumpdata base.sharedcategories --indent 2 > ./website/fixtures/base/sharedcategories.json
python3 ./website/manage.py dumpdata base.sitesocialurls --indent 2 > ./website/fixtures/base/sitesocialurls.json
python3 ./website/manage.py dumpdata base.siteurls --indent 2 > ./website/fixtures/base/siteurls.json
python3 ./website/manage.py dumpdata base.sitecustomization --indent 2 > ./website/fixtures/base/sitecustomization.json

# GisManager
echo "- make fixtures for GisManager"
python3 ./website/manage.py dumpdata gismanager.geoserverurl --indent 2 > ./website/fixtures/gismanager/geoserverurl.json
python3 ./website/manage.py dumpdata gismanager.ogclayer --indent 2 > ./website/fixtures/gismanager/ogclayer.json
python3 ./website/manage.py dumpdata gismanager.basemapprovider --indent 2 > ./website/fixtures/gismanager/basemapprovider.json
python3 ./website/manage.py dumpdata gismanager.basemap --indent 2 > ./website/fixtures/gismanager/basemap.json
python3 ./website/manage.py dumpdata gismanager.webgisproject --indent 2 > ./website/fixtures/gismanager/webgisproject.json

# Usermanager
echo "- make fixtures for Usermanager"
python3 ./website/manage.py dumpdata usermanager.userprofile --indent 2 > ./website/fixtures/usermanager/userprofile.json

echo "End process"