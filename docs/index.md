![GitHub branch checks state](https://img.shields.io/github/checks-status/MaxDragonheart/OpenGeoData/main?style=for-the-badge)
![GitHub](https://img.shields.io/github/license/MaxDragonheart/OpenGeoData?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/MaxDragonheart/OpenGeoData?style=for-the-badge)
![GitHub milestone](https://img.shields.io/github/milestones/progress/MaxDragonheart/OpenGeoData/1?style=for-the-badge)
![GitHub milestones](https://img.shields.io/github/milestones/open/MaxDragonheart/OpenGeoData?style=for-the-badge)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/MaxDragonheart/OpenGeoData?style=for-the-badge)
![GitHub Release Date](https://img.shields.io/github/release-date/MaxDragonheart/OpenGeoData?style=for-the-badge)
![GitHub (Pre-)Release Date](https://img.shields.io/github/release-date-pre/MaxDragonheart/OpenGeoData?label=Pre-Release%20Date&style=for-the-badge)

# OpenGeoData
OpenSource project focused on sharing of geographic data to citizens and technicians.

<img src="./img/logo.png" alt="OpenGeoData logo" style="width:150px; height:auto;"/>

## About OpenGeoData
OpenGeoData is a project that born with the ambition of became a platform useful to citizens and technicians for share geographic public data.
OpenGeoData use [Django](https://www.djangoproject.com/), born as cloud based platform thanks to [Docker](https://www.docker.com/). 
If you want, use [this Geoserver](https://github.com/MaxDragonheart/docker-geoserver) dockerized version for build you project.

## Building the image
1. Clone the repository: ```git clone git@github.com:MaxDragonheart/OpenGeoData.git```
2. Edit the [env](.env) file with your own settings.
3. Build the image:

    -> Development ```docker-compose -f docker-compose-dev.yml up -d --build```
    
    -> Production ```docker-compose -f docker-compose.yml up -d --build```

4. Run project: ```docker exec -it <containerID> bash```
5. Choice if the project runs with initial data(*a*) or not(*b*).

    a. Use initial demo data: ```./initial_data.sh```

    b. Start empty project:
    ```
    ./build_tables_and_collectstatics.sh
    python3 website/manage.py createsuperuser
    ```
   
6. Share your geographic data :)

## Roadmap
You can see the roadmap [here](https://github.com/MaxDragonheart/OpenGeoData/milestones).
