# Django 
[Site](https://docs.djangoproject.com/en/4.0/)

Start project: `poetry run python3 manage.py runserver`

## Backup | [ref](https://docs.djangoproject.com/en/4.0/ref/django-admin/#dumpdata)
Use [local_backup_fixtures.sh](https://github.com/MaxDragonheart/OpenGeoData/blob/main/website/scripts/local_backup_fixtures.sh) if you are in staging or [backup-fixtures.sh](https://github.com/MaxDragonheart/OpenGeoData/blob/main/website/scripts/backup-fixtures.sh) if you are in production.

## Restore | [ref](https://docs.djangoproject.com/en/4.0/ref/django-admin/#loaddata)
Use [local_restore_fixtures.sh](https://github.com/MaxDragonheart/OpenGeoData/blob/main/website/scripts/local_restore_fixtures.sh) if you are in staging or [restore-fixtures.sh](https://github.com/MaxDragonheart/OpenGeoData/blob/main/website/scripts/restore-fixtures.sh) if you are in production.

## Translation | [ref](https://docs.djangoproject.com/en/4.0/topics/i18n/translation/#localization-how-to-create-language-files)
Make translation file: `poetry run python3 manage.py makemessages -l en`

Translate all: `poetry run python3 manage.py compilemessages`