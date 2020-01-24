# import os
# import logging as lg
import random

# import urllib.parse
# import requests

from .ggl.gmaps import ZGMaps
from .mediawiki import mediawiki
from .query.query import ZQuery


class ZGrandPy:

    def __init__(self):
        pass


_HELLO_ = ["Hello", "Salut", "Comment vas-tu", "Hooo !!!"]
_NICK_NAME_ = ["mon poussin", "mon coeur", "mon petit marshmallow"]
_WELCOME_ = ["ravis de te revoir", "ça me fait tellement plaisir de te revoir", "ton grandpy est toujours heureux de te voir", ]
_PROPOSAL_ = ["quel endroit cherches-tu cette fois?", "quel lieu souhaites-tu visiter cette fois-ci", "où souhaites-tu aller aujourd'hui"]

_HdELLO_ = ["Hello", "Salut", "Comment vas-tu", "Hooo !!!"]


def zparse(query, key):

    place_lst = []

    qry = ZQuery(query)

    # extract specified place/spot from query
    place = qry.spot

    # get place geocoding
    gmaps = ZGMaps(key)
    geocoding_dct = gmaps.geocoding_request(place)

    if geocoding_dct:

        latitude = geocoding_dct['location']['lat']
        longitude = geocoding_dct['location']['lng']

        # get static map
        geocoding_dct['map'] = gmaps.static_map_request_url(latitude, longitude)
        print('maps', geocoding_dct['map'])

        # get reference of description page
        place_lst = mediawiki.wikipedia_request_page_from_geocoding(latitude, longitude)
        print("place_lst", place_lst)

        # extract place description
        if place_lst:

            nplace = len(place_lst)
            nplace_max = 3

            idx_max = min(nplace, nplace_max)
            print(idx_max)

            place = random.choice(place_lst[:idx_max])

            description = mediawiki.wikipedia_extract_page(place['pageid'])
            geocoding_dct['description'] = description

            print("description app:", description)

    return geocoding_dct


def welcome():

    hello = random.choice(_HELLO_)
    nick = random.choice(_NICK_NAME_)
    welcome = random.choice(_WELCOME_)
    proposal = random.choice(_PROPOSAL_)

    return hello + " " + nick + ", " + welcome + " ! " + proposal + " ?"


def parse():

    print("dummy for test")
    print("other dummy thing for test")
    pass


if __name__ == "__main__":

    gmaps_geocoding('cité la meynard', 'azerfghjkl51654mlkghfch')
