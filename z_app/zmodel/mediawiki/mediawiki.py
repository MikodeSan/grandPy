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

# import urllib.parse
import requests


__WIKIPEDiA_URL__ = "https://fr.wikipedia.org/w/api.php"
__RADIUS_MIN__ = 10
__RADIUS_DEFAULT__ = 1700
__RADIUS_MAX__ = 10000
__GS_LIMIT_MIN__ = 1
__GS_LIMIT_DEFAULT__ = 7
__GS_LIMIT_MAX__ = 500


def wikipedia_request_page_from_geocoding(flatitude, flongitude):
    """ Get list of wikipedia page identifiers related to the specified geocode """

    places_list = []

    loc = "{}|{}".format(flatitude, flongitude)
    print(loc)

    parameters = {
        "action": "query",
        "list": "geosearch",
        "gscoord": loc,
        "gsradius": __RADIUS_DEFAULT__,
        "gslimit": __GS_LIMIT_DEFAULT__,
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


def wikipedia_extract_page(pageid):
    """ Extract description text from the specified wikipedia page """

    # cite paradis, paris; pageid 5653202 for test
    description = ""

    parameters = {
        "action": "query",
        "pageids": pageid,
        "prop": "extracts",
        #"exintro": "true",
        "exsentences": 3,
        "explaintext": "true",
        "exsectionformat": "wiki",
        "format": "json",
    }

    # API Request
    response = requests.get(url=__WIKIPEDiA_URL__, params=parameters)

    if response.status_code == 200:

        reply_dict = response.json()

        description = reply_dict['query']['pages'][str(pageid)]['extract']
        # print("description:", description)

        stop_section_lst = ['références', 'bibliographie', 'annexes', 'notes', 'voir aussi']
        enable = True

        if description:

            idx = 0
            desc_lst = []
            str_tmp = description.split("\n\n==", 1)
            while str_tmp and enable:

                # print(idx, "str_tmp:", str_tmp)
                desc_lst.append(str_tmp.pop(0).replace("\n", "<br/>"))
                # print(idx, "desc:", desc_lst)
                # print(idx, "str_tmp:", str_tmp)

                if str_tmp:
                    str_tmp = str_tmp[0].split("==\n", 1)
                    section_title = str_tmp.pop(0)
                    section_title = section_title.lower()


                    if any(section in section_title for section in stop_section_lst):
                        print("Stop section found")
                        enable = False
                    else:
                        str_tmp = str_tmp[0].split("\n\n==", 1)

                idx += 1

            for idx, desc in enumerate(desc_lst):
                print(idx, desc)

            description = ''.join(desc_lst)

        else:
            print('wikimedia page not found')
            lg.warning('wikimedia page not found')
    else:
        print('mediawiki reply error')
        lg.warning('mediawiki reply error')

    del response

    return description


if __name__ == "__main__":

    import logging as lg

    lg.basicConfig(format='P%(process)s-T%(asctime)s.%(msecs)03d-%(name)s-%(levelname)s: %(message)s', datefmt='%H:%M:%S', level=lg.DEBUG)

    lg.critical('critical')
    lg.error('error')
    lg.warning('warning')
    lg.info('info')
    lg.debug('debug')

    wikipedia_request_page_from_geocoding(48.8749731, 2.3498414)
