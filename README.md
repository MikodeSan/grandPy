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

On submit event (~~enter key pressed or submit image click~~), the user's query is catched from input form and displayed into the dialog box as a text block. The `innerHTML` method is used to update the view content without refresh the web page.
Then, a spinner animation is started to simulate Grand-Py's reflection at the same time the query is sent as form data to flask server via a AJAX post request.

When the response is received asynchronously from the server, the callback function extracts the received JSON-formatted data and displays the Grand-Py's reply and the defined map if necessary into the dialog box.

### Back-end

#### Query analysis: identification of requested place

The goal is to identify the requested place from the user's query sent by the front-end side.

The punctuations signs defined in the `string` class and the most common [_French_ stop words](https://github.com/6/stopwords-json/blob/master/dist/fr.json) are discarded from the sentence. In addition, a list of specific stop words such as [adresse, situe, où est, trouve, cherche, aller, connais] are defined to delimit text block that could be a requested place.
Finally, the only one remaining text block is considered as the searched location. If more than one text block are remaining, a random pre-defined Grand-Py's reply is returned to the front-end, telling the query is not understood.

#### Localization of a specified place/site

#### Geocoding

The [Google Maps Geocoding API](https://developers.google.com/maps/documentation/geocoding) is used to locate the identified place.  
The site name is sent to the geocoding service via a HTTP request, as a result the standard address and the coordinates (longitude/latitude) are returned as JSON-formatted data.
In order to improve localization result, taking into account that the user is French, the local language as '_french_' and the preferential search region as ccTLD code '_fr_' are also specified to the service.

#### Map

By Knowing the geocode (coodinates), the relative map can be got sending a HTTP request to the [Google Maps Static API](https://developers.google.com/maps/documentation/maps-static). By specifying to the service some parameters like image size, zoom level and coordinates of the pin, as a result the image url of a static map (non-interactive) are returned.  
Then this url can be transfered to the front-end side (without the Google key for security).

#### Intéraction Media Wiki

The geocode is also used to get back points of interest from [MediaWiki service](https://www.mediawiki.org/wiki/API:Main_page). By sending to the service a HTTP `GET` request as `action query`, specifying the _coordinates_ and the _maximal perimeter_, a list of Wikipedia page identifiers is returned sorted by distance from specified coordinates. So, a random page can be selected in order to return Grand-Py's replies more diversified for the same user's query.

With another request speciying the selected _page identifier_, the page text of the point of interest is returned. So, by discarding titles, the first sentences is extracted and used to complete the Grand-Py's reply to the user.

#### random reply

For each Grand-Py's reply, predefined text is randomly selected to embellish the information returned to the user.

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

- [Webapp](https://z-grand-py.herokuapp.com/zapp)
- [PivotalTracker](https://www.pivotaltracker.com/n/projects/2419153)
- [Github](https://github.com/MikodeSan/grandPy)
