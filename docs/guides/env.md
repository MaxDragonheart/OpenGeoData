# Project Environment

The project use `.env` with the key below:
```markdown
SECRET_KEY='YOUR-SECRET-KEY'
DB_ENGINE=django.contrib.gis.db.backends.postgis
ALLOWED_HOSTS=127.0.0.1, localhost
CSRF_TRUSTED_ORIGINS=['http://domin.io', 'https://domin.io']
DEBUG=0
DB_NAME=YOUR-DB_NAME
DB_USER=YOUR-DB_USER
DB_PASSWORD=YOUR-DB_PASSWORD
DB_HOST=YOUR-DB_HOST
DB_PORT=YOUR-DB_PORT

# Personal Initial Data[Optional]
ADMIN_USERNAME=
ADMIN_PASSWORD=
DOMAIN_NAME=
DOMAIN=
SITE_TITLE=
SITE_LOGO=
SITE_DESCRIPTION=
ADDRESS=
CONTACT_PHONE=
CONTACT_EMAIL=
CONTACT_OFFICIAL_EMAIL=
```
To generate secret key you can use [Djecrety](https://djecrety.ir/)