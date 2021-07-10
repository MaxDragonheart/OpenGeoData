# UfficioUrbanistica
Sito web dell'Ufficio Urbanistica del Comune di Parete


## Utilità
### Gestione requirements
Per creare la lista dei packages:

        pip3 freeze > requirements.txt

Per installare i packages da requirementes.txt:

        pip3 install -r requirements.txt

### Comandi git
Mettere cartella o file in .gitignore: `echo "nome_cartella" >> .gitignore`

Rimuovere cartella o file da git: `git rm -r --cached nome_cartella`

Procedura per push:

      git status
      git add .
      git commit -am "MESSAGGIO"
      git push origin master