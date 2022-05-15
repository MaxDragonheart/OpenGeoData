# Django 
[Site](https://docs.djangoproject.com/en/4.0/)

Start project: `poetry run python3 manage.py runserver`

## Backup
- Usermanager
```markdown
python3 manage.py dumpdata usermanager.userprofile --indent 2 > fixtures/usermanager/userprofile.json
```
- Base
```markdown
python3 manage.py dumpdata sites --indent 2 > fixtures/base/sites.json
python3 manage.py dumpdata base.sitesocialurls --indent 2 > fixtures/base/sitesocialurls.json
python3 manage.py dumpdata base.siteurls --indent 2 > fixtures/base/siteurls.json
python3 manage.py dumpdata base.sitecustomization --indent 2 > fixtures/base/sitecustomization.json
```

## Restore

### Globale
```markdown
python3 manage.py loaddata fixtures/**/*.json
```
## Translation | [ref](https://docs.djangoproject.com/en/4.0/topics/i18n/translation/#localization-how-to-create-language-files)
Make translation file: `poetry run python3 manage.py makemessages -l en`
Translate all: `poetry run python3 manage.py compilemessages`