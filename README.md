# Grand-Py web application

## Context

The application allows to find the address of a place specified by the user and give also a little description of an interesting site around. The Google Maps and Wiki Media services is used.

## Features

- __Navigation__: From the '_Home_' page, the '_App_' page is displayed by clicking on a link.
- __Dialog view__: The user's query is keyed into a text input field and a dialog box displays the user's query and Grand-Py's reply like a chat messages.
- __Identification of the searched place__: the specified place is identified from the user's query sentence.
- __Localization__: Find the address, the coordinate and the map of a specified place.
- __Place description__: Get description of a point of interest near the specified place.
- __Online hosting__: Access the online web application.

## Architecture

### Front-end

#### HTMM / CSS

##### Body layout

- Header: Logo, title and pickupline
- Central zone content:
  - The Dialog box is a void zone displaying and distinguishing Grand-Py and user messages.
    - Spinner / Loader is an infinite loop animation coordinated by keyframes. The animation will be interrupted asynchronously according to AJAX request.
  - The query field is compounded of a text input to keyed the query and a submit button to validate and send the user's query.
- Footer:
  - Names
  - Link: contact, source code (Github repository), project plan, social network.
- Responsiveness: Define maximal and minimal block size and use CSS flex property.

#### JavaScript

- press 'Enter' key and without refresh the web page
  - récupération de la requete

Interactions en AJAX
fonction post et get avec callback

sans recharger la page > innerHTML
ajoute block et text dynamiquement

### Back-end

#### Analyse de requete

- Analyse requête, identification adresse
  - stop word

#### interaction Google Maps

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

#### Intéraction Media Wiki

- interogation WIKI avec geocode
  - récupère site par ordre de proximité
  - sélection aléatoire parmi les 7 premiers sites
  - extraction de la descripion du site , mes 3 premières phrases
  - suppression des titres, pour les pages tres courtes

#### Hosting

- As a user, I want to  > Prod
  - configure heroku
  - variable d'environnement : clé google

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
