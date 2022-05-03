# Devasc_Skills

# Task 1: Python experiments
## Taakvoorbereiding en taakimplementatie
Prerequisites:
* Geopy
* datetime
* folium

Installeren met pip install 
Geüpdatete Linux
* sudo apt-get update
* sudo apt-get upgrade

Gebruik maken van python/jupyter/visual studio code

![image](https://user-images.githubusercontent.com/99889045/166420214-8cfabd26-e97f-4655-bb5e-f3080bb3918d.png)


## Taak oplossen van van problemen
## Taakverificatie
# Task 2: Explore Python development tool and REST APIs
## Taakvoorbereiding en taakimplementatie
Directory van locale python environment.

Which python3 o /usr/bin/python3
Virtuele omgeving maken voor Python3:

cd labs/devnet-src:python/
python3 -m venv devfun o -m venv  virtuele omgeving maken waarbij devfun de naam is van die omgeving
Activeren virtuele omgeving:

Source devfun/bin/activate o Hiermee start je de virtuele omgeving devfun op, zichtbaar door vanvoor (devfun)
Huidige packages checken in het systeem environment (volledige environment)

Python3 -m pip freeze | grep requests o Grep = specifiek zoeken naar alles met requests Virtuele omgeving delen
Pip3 freeze > requirements.txt o Huidige requirements opslaan in txt bestand
Pip3 install -r requirements.txt o Requirements installeren in een andere virtuele omgeving
Task 2: Explore rest APIs with API Simulator and Postman

Curl = hier krijg je dezelfde informatie als voor de /books API Request URL: deze URL wordt gebruikt in de API request  gebruiken om dezelfde info te krijgen als met curl, Postman en Python Code: HTTP response code

100 = informational response
200 = successfull response
300 = redirection response
400 = client error response
500 = server error response
Token achterhalen: API = POST /loginViaBasic

Try it out + execute = inloggen
Response body geeft token
Boek toevoegen via Postman:

POST + request URL
Authorization  Type = API key
Key = X-API-KEY  (opgehaald hierboven)
Body = raw knop  text veranderen naar JSON
JSON object toevoegen (naar keuze, in JSON format)

## Taak oplossen van van problemen
## Taakverificatie

# Task 3: Github Skills
## Taakvoorbereiding en taakimplementatie
mkdir voor de verschillende mappen

git init: map initialiseren bestand aanmaken + stagen : git add readme.md git commit -m "bericht" : uploadn van het bestand

nieuwe repo koppelen aan github repo: git remote add origin https://github.com/Svesto/Devasc_Skills.git

uploaden:

git push origin master
## Taak oplossen van van problemen
## Taakverificatie

# Task 4: Webex Teams API

## Taakvoorbereiding en taakimplementatie: 
Prerequisites:

python3
Implementatie:

Bestaande scripts aanpassen (zie uploads) Nodig voor aanpassing:
Access_Token (via developer.webex.com)
Room_ID
Person_email


Opmerkingen: 
Probleem wat vaak voorkwam mbt pushen van data: 
error: failed to push some refs to 'https://github.com/Svesto/Devasc_Skills.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

Oplossing: 
git pull --rebase https://github.com/Svesto/Devasc_Skills
hierdoor wordt het terug mogelijk om data te pushen

## Taak oplossen van van problemen
## Taakverificatie

# Task 5: Data Format Conversion
## Taakvoorbereiding en taakimplementatie:
## Taak oplossen van van problemen
## Taakverificatie
