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