# UfficioUrbanistica
## Project Environment
The project use `.env` with the key below:
```markdown
SECRET_KEY='YOUR-SECRET-KEY'
DB_ENGINE=django.contrib.gis.db.backends.postgis
ALLOWED_HOSTS=127.0.0.1, localhost
DEBUG=1
DB_NAME=YOUR-DB_NAME
DB_USER=YOUR-DB_USER
DB_PASSWORD=YOUR-DB_PASSWORD
DB_HOST=YOUR-DB_HOST
DB_PORT=YOUR-DB_PORT
```

## Utilità

### Comandi git
Mettere cartella o file in .gitignore: `echo "nome_cartella" >> .gitignore`

Rimuovere cartella o file da git: `git rm -r --cached nome_cartella`

Procedura per push:

      git status
      git add .
      git commit -am "MESSAGGIO"
      git push origin master