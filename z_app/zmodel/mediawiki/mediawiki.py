#!/usr/bin/python3
"""
    geosearch.py

    MediaWiki API Demos
    Demo of `Geosearch` module: Search for wiki pages nearby

    MIT License
"""

import os
import logging as lg
import shutil

import urllib.parse
import requests


__WIKIPEDiA_URL__ = "https://fr.wikipedia.org/w/api.php"
__RADIUS_MIN__ = 10
__RADIUS_DEFAULT__ = 1250
__RADIUS_MAX__ = 10000
__GS_LIMIT_MIN__ = 1
__GS_LIMIT_DEFAULT__ = 12
__GS_LIMIT_MAX__ = 500


def wikipedia_request_page_from_geocoding(flatitude, flongitude):

    places_list = []

    loc = "{}|{}".format(flatitude, flongitude)
    print(loc)

    radius = "{}".format(__RADIUS_MAX__)          # radius unit in meter
    print(radius)

    parameters = {
        "action": "query",
        "list": "geosearch",
        "gscoord": loc,
        "gsradius": __RADIUS_MAX__,
        "gslimit": __GS_LIMIT_MAX__,
        "format": "json",
    }

    # API Request
    response = requests.get(url=__WIKIPEDiA_URL__, params=parameters)

    if response.status_code == 200:

        reply_dict = response.json()

        places_list = reply_dict['query']['geosearch']

        if places_list:

            for idx, place in enumerate(places_list):
                print(idx, "W#{}".format(place['pageid']), place['title'], place['dist'], "m")

        else:
            print('address not found')
            lg.warning('address not found')
    else:
        print('mediawiki reply error')
        lg.warning('mediawiki reply error')

    del response

    return places_list


class ZMediaWiki:

    def __init__(self):
        pass

    def get(self):
        """Search for pages by specifying the geographic coordinates"""

        pass


# def gmaps_static_map_request(location, key):

#     map_url = gmaps_static_map_request_url(location, key)
#     print(map_url)

#     # Store static map image into temporary directory
#     response = requests.get(map_url, stream=True)
#     if response.status_code == 200:
#         image_path = __TMP_PATH__ + "/{}".format("map.png")
#         # print(image_path)
#         with open(image_path, 'wb') as out_file:
#             response.raw.decode_content = True
#             shutil.copyfileobj(response.raw, out_file)
#     else:
#         print('google static map error')

#     del response

# def gmaps_static_map_request_url(location, key):

#     lat = location['lat']
#     lng = location['lng']
#     loc = "{},{}".format(lat, lng)
#     print(loc)
#     size = "{}x{}".format(240, 240)     # IPhone [480 × 320] ; standard_min [320 x 200|240]
#     print(size)
#     markers = []
#     pin = "color:blue|label:P|{},{}".format(lat,lng)
#     print(pin)
#     markers.append(pin)
#     params = {'center': loc, 'zoom': 15, 'size': size, 'maptype': 'roadmap', 'markers': markers, 'key': key}
#     url = __GMAPS_STATIC_MAP_URL__ + urllib.parse.urlencode(params, doseq=True)
#     # print(url)
#     return url

# def parse():
#     pass

if __name__ == "__main__":

    import logging as lg

    # logger = logging.getLogger()
    # formatter = logging.Formatter('P%(process)s-T%(asctime)s-%(name)s-%(levelname)s-%(message)s')
    # logger.setFormatter(formatter)
    # logger.setLevel(logging.DEBUG)
    lg.basicConfig(format='P%(process)s-T%(asctime)s.%(msecs)03d-%(name)s-%(levelname)s: %(message)s', datefmt='%H:%M:%S', level=lg.DEBUG)


    # logger.critical('critical')
    # logger.error('error')
    # logger.warning('warning')
    # logger.info('info')
    # logger.debug('debug')

    lg.critical('critical')
    lg.error('error')
    lg.warning('warning')
    lg.info('info')
    lg.debug('debug')

    loc = {
        "lat": 46.084044,
        "lng": 6.728173
    }

    wikpedia_request_page_from_geocoding(loc)

    # gmaps_geocoding('cité la meynard', 'azerfghjkl51654mlkghfch')
