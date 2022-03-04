# OpenGeoData
OpenSource project focused on sharing of geographic data to citizens and technicians.

<img src="./img/logo.png" alt="OpenGeoData logo" style="width:150px; height:auto;"/>

## About OpenGeoData
OpenGeoData is a project that born with the ambition of became a platform useful to citizens and technicians for share geographic public data.
OpenGeoData use [Django](https://www.djangoproject.com/), born as cloud based platform thanks to [Docker](https://www.docker.com/). 

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
