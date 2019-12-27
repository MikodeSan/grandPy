import logging as lg

import urllib.parse


__GMAPS_URL__ = 'https://maps.googleapis.com/maps/api/geocode/json?'

class ZGrandPy:

    def __init__(self):
        
        pass

def gmaps_geocoding(query, key):

    params = {'address': query, 'key': key}
    url = __GMAPS_URL__ + urllib.parse.urlencode(params)
    print(url)
    return url
    
def parse():
    pass

def default_url():

    query = 'Hellö Wörld@Python'
    
    url = urllib.parse.quote_plus(query)
    print(url)
    lg.info(url)

    print(url)


 

if __name__ == "__main__":
    
    gmaps_geocoding('cité la meynard', 'azerfghjkl51654mlkghfch')

