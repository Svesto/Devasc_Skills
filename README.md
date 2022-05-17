# Devasc_Skills

# Task 1: Python experiments
## Taakvoorbereiding en taakimplementatie
Prerequisites:
* Geopy
* datetime
* folium
* VM machine voor DEVASC-skills
* Scripts te vinden bij taak 1

Installeren met pip install 

Geüpdatete Linux
* sudo apt-get update
* sudo apt-get upgrade

Gebruik maken van python/jupyter/visual studio code


## Taak oplossen van problemen
Probleem: Niet de juiste versie van IDLE Shell gebruiken
Oplossing: Gebruik Versie met Python 3.8


## Taakverificatie
https://github.com/Svesto/Devasc_Skills/tree/master/Task1

# Task 2: Explore Python development tool and REST APIs
## Taakvoorbereiding en taakimplementatie
Prerequisites:
* VM machine voor DEVASC-skills
* Python 3.8.10
* School Library web page --> http://library.demo.local/
* School Library API --> http://library.demo.local/api/v1/docs
* Postman --> -	https://dl.pstmn.io/download/latest/linux64
* Scripts te vinden bij taak 2

## Taakverificatie
Verificatie van verschillende scriptjes op Postman: 
https://github.com/Svesto/Devasc_Skills/tree/master/Task2

# Task 3: Github Skills
## Taakvoorbereiding en taakimplementatie
Prerequisites:
* VM machine voor DEVASC-skills
* Github account
* Repository creatie (Devasc_Skills)
* Lokale repository verbinden met online repository
* Github token voor inlog
## Taak oplossen van van problemen
* Inloggen gaat niet met lokaal account
  * Ophalen bij Github zelf onder settings/developer settings
## Taakverificatie
Git status
Controle https://github.com/Svesto/Devasc_Skills
https://github.com/Svesto/Devasc_Skills/tree/master/Task3

# Task 4: Webex Teams API

## Taakvoorbereiding en taakimplementatie: 
Prerequisites:
* VM machine voor DEVASC-skills
* python3
* API Documentation --> https://developer.webex.com/
* Personal access Token --> https://developer.webex.com/docs/getting-started#accounts-and-authentication
* Scripts te vinden onder taak 3
* Room_ID (via script)
* Person_email (via script)
* Visual Studio Code

## Taak oplossen van problemen 
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


## Taakverificatie
https://github.com/Svesto/Devasc_Skills/tree/master/Task4

# Task 5: Data Format Conversion
## Taakvoorbereiding en taakimplementatie:
Prerequisites:
* VM machine voor DEVASC-skills
* python3
* Python script --> https://github.com/wleppens/PythonExperiments/edit/main/json/json_convert.py
* Aanpassing van script door print statements

## Taak oplossen van problemen
Commentaar weghalen, en print statements toevoegen
## Taakverificatie
https://github.com/Svesto/Devasc_Skills/tree/master/Task5


# Task 7: Network Documenttion
## Taakvoorbereiding en taakimplementatie: 
Tekeningsoftware: Draw-io = https://app.diagrams.net/
VLAN-segmentatie: 
* Bepaling hoeveelheid VLANs
* Logische verdeling
* Bepaling IP-ranges

### Guide Draw-io
* Draw-io docx file

## Taak oplossen van problemen
N.V.T.

## Taakverificatie
Implementatie werkt op live systeem

# Task 8: Netmiko
## Taakvoorbereiding en taakimplementatie
Prerequisites: 
* Visual Studio Code
* Python v3.8
* VM machine voor DEVASC-skills
* User: Admin
* Pass: cisco
* IP-adres: 192.168.10.97

Config bestand: https://github.com/Svesto/Devasc_Skills/blob/master/Task8%20-%20Netmiko/config.txt
Script: https://github.com/Svesto/Devasc_Skills/blob/master/Task8%20-%20Netmiko/configpush_via_txt.py

## Taak oplossen van problemen
Bepaling van IP-adres: 
* WIFI uit
* cmd: ipconfig /all, default gateway --> ip-adres switch

Juiste statements voor running config: 
* running=cisco_Switch.send_command("show run")

## Taakverificatie
Script: 
* running=cisco_Switch.send_command("show run")
* print (running)
Resultaat: configuratie van config.txt is toegepast 
https://github.com/Svesto/Devasc_Skills/blob/master/Task8%20-%20Netmiko/Task%208%20result.png


