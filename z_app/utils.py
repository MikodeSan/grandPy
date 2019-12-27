import os
import logging as lg
import shutil

import urllib.parse
import requests


__GMAPS_GEOCODING_URL__ = 'https://maps.googleapis.com/maps/api/geocode/json?'
__GMAPS_STATIC_MAP_URL__ = 'https://maps.googleapis.com/maps/api/staticmap?'

__TMP_PATH__ = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tmp')

class ZGrandPy:

    def __init__(self):
        
        pass

def gmaps_geocoding_request(query, key):

    request_url = gmaps_geocoding_request_url(query, key)

    geocoding_dict = {}

    response = requests.get(request_url)
    if response.status_code == 200:

        reply_dict = response.json()
        if reply_dict['results'] and reply_dict['status'] == "OK":

            location_dict = reply_dict['results'][0]['geometry']['location']
            # print(location_dict)

            gmaps_static_map_request(location_dict, key)

            geocoding_dict = reply_dict
        else:
            print('address not found')
    else:
        print('google reply error')

    del response

    return geocoding_dict


def gmaps_geocoding_request_url(query, key):

    params = {'address': query, 'key': key}
    url = __GMAPS_GEOCODING_URL__ + urllib.parse.urlencode(params)
    # print(url)
    return url
    

def gmaps_static_map_request(location, key):

    map_url = gmaps_static_map_request_url(location, key)
    print(map_url)

    # Store static map image into temporary directory  
    response = requests.get(map_url, stream=True)
    if response.status_code == 200:
        image_path = __TMP_PATH__ + "/{}".format("map.png")
        # print(image_path)
        with open(image_path, 'wb') as out_file:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, out_file)
    else:
        print('google static map error')

    del response

def gmaps_static_map_request_url(location, key):

    lat = location['lat']
    lng = location['lng']
    loc = "{},{}".format(lat, lng)
    print(loc)
    size = "{}x{}".format(240, 240)     # IPhone [480 × 320] ; standard_min [320 x 200|240]
    print(size)
    markers = []
    pin = "color:blue|label:P|{},{}".format(lat,lng)
    print(pin)
    markers.append(pin)
    params = {'center': loc, 'zoom': 13, 'size': size, 'maptype': 'roadmap', 'markers': markers, 'key': key}
    url = __GMAPS_STATIC_MAP_URL__ + urllib.parse.urlencode(params, doseq=True)
    # print(url)
    return url

def parse():
    
    pass

if __name__ == "__main__":
    
    gmaps_geocoding('cité la meynard', 'azerfghjkl51654mlkghfch')

