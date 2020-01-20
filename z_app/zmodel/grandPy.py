# import os
# import logging as lg
import random

# import urllib.parse
# import requests

from .ggl.gmaps import gmaps_geocoding_request
from .mediawiki import mediawiki
from .query.query import ZQuery


class ZGrandPy:

    def __init__(self):
        pass


def zparse(query, key):

    reply_dct = {}
    reply_dct['address'] = ""
    reply_dct['location'] = {}
    reply_dct['description'] = ""

    place_lst = []

    qry = ZQuery()

    query = "donne moi l'adresse de paris"
    place = qry.extract_place(query)

    # get place geocoding
    geocoding_dct = gmaps_geocoding_request(place, key)

    # get place description
    if geocoding_dct:

        result = geocoding_dct['results'][0]

        address = result['formatted_address']

        reply_dct['address'] = address

        location = result['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        reply_dct['location'] = {'lat': latitude, 'lng': longitude}

        # place page reference
        place_lst = mediawiki.wikipedia_request_page_from_geocoding(latitude, longitude)
        print("place_lst", place_lst)

        # place description
        if place_lst:

            nplace = len(place_lst)
            nplace_max = 3

            idx_max = min(nplace, nplace_max)
            print(idx_max)

            place = random.choice(place_lst[:idx_max])

            description = mediawiki.wikipedia_extract_page(place['pageid'])
            reply_dct['description'] = description

            print("description app:", description)

    return reply_dct



def parse():

    print("dummy for test")
    print("other dummy thing for test")
    pass


if __name__ == "__main__":

    gmaps_geocoding('cité la meynard', 'azerfghjkl51654mlkghfch')
