import os
import logging as lg
import shutil
import random

import urllib.parse
import requests

from .mediawiki import mediawiki


__GMAPS_GEOCODING_URL__ = 'https://maps.googleapis.com/maps/api/geocode/json?'
__GMAPS_STATIC_MAP_URL__ = 'https://maps.googleapis.com/maps/api/staticmap?'

__TMP_PATH__ = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static', 'tmp')


class ZGrandPy:

    def __init__(self):
        pass


def zparse(query, key):

    reply_dct = {}
    reply_dct['address'] = ""
    reply_dct['location'] = {}
    reply_dct['description'] = ""

    place_lst = []


    # get place geocoding
    geocoding_dct = gmaps_geocoding_request(query, key)

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
