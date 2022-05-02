# syntax=docker/dockerfile:1
ARG PROJECT_NAME=test_dev

# Official Ubuntu Image as Layer
FROM gisconsultant/ulgis as gis-os
# Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive

# GIS-OS as Layer
FROM gis-os as project-dependencies
# Set work directory
WORKDIR /app/web
# Environment variables
ARG PROJECT_NAME=personalwebsite
ENV ENV_NAME=${PROJECT_NAME} \
    # Pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # Poetry
    # https://python-poetry.org/docs/configuration/#using-environment-variables
    POETRY_VERSION=1.1.11
# Install Poetry
RUN pip3 install "poetry==$POETRY_VERSION"
# Copy project requirements
COPY ./pyproject.toml ./pyproject.toml
# Project initialization
RUN poetry config virtualenvs.create false \
  && poetry install $(test "$ENV_NAME" == production && echo "--no-dev") --no-interaction --no-ansi

# PROJECT-DEPENDENCIES as Layer
FROM project-dependencies as opengeodataproject
ARG DEBUG=on
ARG ALLOWED_HOSTS=*
ARG SECRET_KEY=django-insecure-#vvw^xj9ri$bioj8d1j7rr@dy!$656rxq=!$4a^6dlqlav7-(f
ARG DB_ENGINE=django.contrib.gis.db.backends.postgis
ARG DB_NAME=test_db_docker
ARG DB_USER=postgres
ARG DB_PASSWORD=1983
ARG DB_PORT=5432
ARG DB_HOST=localhost
ARG PROJECT_PORT=1983

ENV SECRET_KEY=${SECRET_KEY} \
    DB_ENGINE=${DB_ENGINE} \
    DB_NAME=${DB_NAME} \
    DB_USER=${DB_USER} \
    DB_PASSWORD=${DB_PASSWORD} \
    DB_PORT=${DB_PORT} \
    DB_HOST=${DB_HOST} \
    DEBUG=${DEBUG} \
    ALLOWED_HOSTS=${ALLOWED_HOSTS} \
    PROJECT_PORT=${PROJECT_PORT} \
    ADMIN_USERNAME=${ADMIN_USERNAME} \
    ADMIN_PASSWORD=${ADMIN_PASSWORD} \
    DOMAIN_NAME=${DOMAIN_NAME} \
    DOMAIN=${DOMAIN} \
    SITE_TITLE=${SITE_TITLE} \
    SITE_LOGO=${SITE_LOGO} \
    SITE_DESCRIPTION=${SITE_DESCRIPTION} \
    ADDRESS=${ADDRESS} \
    CONTACT_PHONE=${CONTACT_PHONE} \
    CONTACT_EMAIL=${CONTACT_EMAIL} \
    CONTACT_OFFICIAL_EMAIL=${CONTACT_OFFICIAL_EMAIL}

# Create project directories
RUN mkdir -p website static-folder media-folder
# Copy project data
COPY website website
RUN rm -rf website/fixtures
COPY fixtures ./website/fixtures
COPY media-folder/default media-folder/default
COPY scripts/migrate-collectstic.sh ./migrate-collectstic.sh
COPY scripts/backup-fixtures.sh ./backup-fixtures.sh
COPY scripts/restore-fixtures.sh ./restore-fixtures.sh
RUN chmod +x **.sh

# OPENGEODATAPROJECT as Layer
FROM opengeodataproject as gunicorn-setting-up
# Install Gunicorn
RUN poetry add gunicorn
# Create directory for logging files
RUN mkdir logs
# Copy adn active entrypoint
COPY scripts/entrypoint.sh ./entrypoint.sh
RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]