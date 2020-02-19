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

#### HTML / CSS: Content and layout

- Header: Logo, title and pickupline
- Central zone content:
  - The Dialog box is a void zone displaying and distinguishing Grand-Py and user messages.
    - Spinner / Loader is an infinite loop animation coordinated by keyframes. The animation will be interrupted asynchronously according to AJAX request.
  - The query field is compounded of a text input to keyed the query and a submit button to validate and send the user's query.
- Footer: Names and links to contact, source code (Github repository), project plan and social network.
- Responsiveness: Maximal and minimal block size are defined and CSS flex property is used to stretch block if necessary.

#### JavaScript: Dynamic update of the application view and interface (data exchange) with the back-end

On submit event (~~enter key pressed or submit image click~~), the user's query is catched from input form and displayed into the dialog box as a text block. The ```innerHTML``` method is used to update the view content without refresh the web page.
Then, a spinner animation is started to simulate Grand-Py's reflection at the same time the query is sent as form data to flask server via a AJAX post request.

When the response is received asynchronously from the server, the callback function extracts the received JSON-formatted data and displays the Grand-Py's reply and the defined map if necessary into the dialog box.

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

#### random reply

#### Hosting

- As a user, I want to  > Prod
  - configure heroku
  - variable d'environnement : clé google

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
