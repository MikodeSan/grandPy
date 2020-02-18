# Grand-Py web application

## Context

The application allows to find the address of a place specified by the user and give also a little description of an interesting site around. The Google Maps and Wiki Media services is used.

## Features

- __Navigation__: From the '_Home_' page, Go to the '_app_' page by clicking on the link and see the application interface.
- __Dialog view__: As a user, I want to see my query displayed into the dialog field by press 'Enter' key and without refresh the web page
  - récupération de la requete
  - affichage requête + réponse dans la zone de dialogue
  - spinner / loader attente réponse
- __Identification of the specified place__:
  - Analyse requête, identification adresse
    - stop word
- __Location__: As a user, I want to get the address and coordonate of a specified place
  - Address
  - Map: get the location displayed into a map
    - format de la map
      - taille + pin
      - retour de l'adresse sans la clé
  - interogation GMAPS geocode
    - adresse formaté + géocode: longitude + latitude
  - interogation GMAPS static map
  - retour réponse par JSON
  - Réponse aléatoire
- __Place description__: get description of the specified address
  - interogation WIKI avec geocode
    - récupère site par ordre de proximité
    - sélection aléatoire parmi les 7 premiers sites
    - extraction de la descripion du site , mes 3 premières phrases
    - suppression des titres, pour les pages tres courtes
- __Online hosting__
  - As a user, I want to access the app/site on web > Prod
    - configure heroku
    - variable d'environnement : clé google

## Architecture

### Front-end

#### HTMM/CSS

Mise en page

- header : logo et phrase d'accroche
- zone centrale :
  - zone vide (qui servira à afficher le dialogue)
  - champ de formulaire pour envoyer une question.
- footer

  - votre prénom & nom
  - lien vers votre
    - repository Github
    - réseaux sociaux

- Responsive
  - utilisation des tailles min max
  - block flex

#### JavaScript

Interactions en AJAX
fonction post et get avec callback

sans recharger la page > innerHTML
ajoute block et text dynamiquement

### Back-end

#### Analyse de requete

#### interaction Google Maps

#### Intéraction Media Wiki

## Algorithm

reponse aléatoire

## Workflow

- Activity diagram
- Processus

## Difficulty

- Solution

## Intégration continue

Tests unitaires

- mock

couverture
linter

## Installation

### Virtual environment

- Create virtual environment named '_venv_' for example
- Activate the new environment
- install requirements from '_requirements.txt_'

### Flask

### Run application

execute : python '_run.py_'

## Links

- Webapp: https://z-grand-py.herokuapp.com/zapp
- PivotalTracker: https://www.pivotaltracker.com/n/projects/2419153
- Github: https://github.com/MikodeSan/grandPy
