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



def parse():

    print("dummy for test")
    print("other dummy thing for test")
    pass


if __name__ == "__main__":

    gmaps_geocoding('cité la meynard', 'azerfghjkl51654mlkghfch')
