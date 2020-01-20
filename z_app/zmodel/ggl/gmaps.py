import os
# import shutil

import logging as lg


import requests
import urllib.parse

lg.basicConfig(format='P%(process)s-T%(asctime)s.%(msecs)03d-%(name)s-%(levelname)s: %(message)s', datefmt='%H:%M:%S', level=lg.DEBUG)


class ZGMaps:

    __GMAPS_GEOCODING_URL__ = 'https://maps.googleapis.com/maps/api/geocode/json?'
    __GMAPS_STATIC_MAP_URL__ = 'https://maps.googleapis.com/maps/api/staticmap?'

    __TMP_PATH__ = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'static', 'tmp')

    def __init__(self, _key):

        self.__key = _key

    def geocoding_request(self, place):

        request_url = self.__geocoding_request_url(place)

        geocoding_dict = {}

        response = requests.get(request_url)
        if response.status_code == 200:

            reply_dict = response.json()

            str = "Reply dict: {}".format(reply_dict)
            lg.debug(str)

            if reply_dict['results'] and reply_dict['status'] == "OK":

                # location_dict = reply_dict['results'][0]['geometry']['location']
                # print(location_dict)

                # gmaps_static_map_request(location_dict, key)

                geocoding_dict = self.__format_geocoding(reply_dict)
            else:
                print('address not found')
        else:
            print('google reply error')

        del response

        return geocoding_dict

    def __geocoding_request_url(self, _place):

        params = {'address': _place, 'language': 'fr', 'key': self.__key}
        url = self.__GMAPS_GEOCODING_URL__ + urllib.parse.urlencode(params)
        # print(url)
        return url

    def __format_geocoding(self, _geo_dct):

        geo_dct = {}

        result = _geo_dct['results'][0]

        geo_dct['address'] = result['formatted_address']

        latitude = result['geometry']['location']['lat']
        longitude = result['geometry']['location']['lng']
        geo_dct['location'] = {'lat': latitude, 'lng': longitude}

        return geo_dct

    # def static_map_request(self, latitude, longitude):

    #     map_url = self.static_map_request_url(latitude, longitude)
    #     print(map_url)

    #     # Store static map image into temporary directory
    #     response = requests.get(map_url, stream=True)
    #     if response.status_code == 200:
    #         image_path = self.__TMP_PATH__ + "\{}".format("map.png")
    #         # print(image_path)

    #         # If file exists, delete it
    #         if os.path.isfile(image_path):
    #             os.remove(image_path)

    #         # Create image file from url
    #         with open(image_path, 'wb') as out_file:
    #             response.raw.decode_content = True
    #             shutil.copyfileobj(response.raw, out_file)
    #     else:
    #         print('google static map error')

    #     del response

    def static_map_request_url(self, _latitude, _longitude):

        loc = "{},{}".format(_latitude, _longitude)
        print(loc)
        size = "{}x{}".format(240, 240)     # IPhone [480 × 320] ; standard_min [320 x 200|240]
        print(size)
        markers = []
        pin = "color:blue|label:P|{},{}".format(_latitude, _longitude)
        print(pin)
        markers.append(pin)
        params = {'center': loc, 'zoom': 15, 'size': size, 'maptype': 'roadmap', 'markers': markers, 'key': self.__key}
        url = self.__GMAPS_STATIC_MAP_URL__ + urllib.parse.urlencode(params, doseq=True)
        # print(url)
        return url
