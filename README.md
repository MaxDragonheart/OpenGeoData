![GitHub branch checks state](https://img.shields.io/github/checks-status/MaxDragonheart/OpenGeoData/main?style=for-the-badge)
![GitHub](https://img.shields.io/github/license/MaxDragonheart/OpenGeoData?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/MaxDragonheart/OpenGeoData?style=for-the-badge)
![GitHub milestones](https://img.shields.io/github/milestones/open/MaxDragonheart/OpenGeoData?style=for-the-badge)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/MaxDragonheart/OpenGeoData?style=for-the-badge)
![GitHub (Pre-)Release Date](https://img.shields.io/github/release-date-pre/MaxDragonheart/OpenGeoData?label=Release%20Date&style=for-the-badge)

# OpenGeoData
OpenSource project focused on sharing of geographic data to citizens and technicians.

<img src="docs/img/logo.png" alt="OpenGeoData logo" style="width:150px; height:auto;"/>

## About OpenGeoData
OpenGeoData is a project that born with the ambition of became a platform useful to citizens and technicians for share geographic public data.
OpenGeoData use [Django](https://www.djangoproject.com/), born as cloud based platform thanks to [Docker](https://www.docker.com/). 
If you want, use [this Geoserver](https://github.com/MaxDragonheart/docker-geoserver) dockerized version for build you project.

## Building the image
1. Clone the repository: ```git clone git@github.com:MaxDragonheart/OpenGeoData.git```
2. Edit the [env](.env) file with your own settings.
3. Build the image:

    -> Staging ```docker-compose -f docker-compose-dev.yml up -d --build```
    
    -> Production ```docker-compose -f docker-compose.yml up -d --build```

4. Run project: ```docker exec -it <containerID> bash```
5. Make DB's tables and collect all statis files:  ```./migrate-collectstic.sh```
6. Share your geographic data :)

## Guide and tips
- Variables for `.env` [here](docs/guides/env.md)
- Handle project with Django [here](docs/guides/django-tips.md)
- Handle project with Poetry [here](docs/guides/poetry-tips.md)
- Useful git tips [here](docs/guides/git-tips.md)
- Initial categories are directly inspired from [INSPIRE](https://inspire-geoportal.ec.europa.eu/theme_selection.html?view=qsTheme)

## Roadmap
You can see the roadmap [here](https://github.com/MaxDragonheart/OpenGeoData/milestones).
