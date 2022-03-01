#!/usr/bin/env bash

## Prepare log files and start outputting logs to stdout
touch ./logs/gunicorn.log
touch ./logs/gunicorn-access.log

cd website

exec gunicorn website.wsgi:application \
    --name website \
    --bind 0.0.0.0:"${PROJECT_PORT}" \
    --workers 3 \
    --log-level=debug \
    --error-logfile=../logs/gunicorn.log \
    --access-logfile=../logs/gunicorn-access.log \
"$@"