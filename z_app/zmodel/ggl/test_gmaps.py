import gmaps as script

import requests

from io import BytesIO
import json


def test_geocoding_return(monkeypatch):

    result_dct = {'results': [{'address_components': [{'long_name': 'Cluses', 'short_name': 'Cluses', 'types': ['locality', 'political']}, {'long_name': 'Haute-Savoie', 'short_name': 'Haute-Savoie', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Auvergne-Rhône-Alpes', 'short_name': 'Auvergne-Rhône-Alpes', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}, {'long_name': '74300', 'short_name': '74300', 'types': ['postal_code']}], 'formatted_address': '74300 Cluses, France', 'geometry': {'bounds': {'northeast': {'lat': 46.08459, 'lng': 6.608080999999999}, 'southwest': {'lat': 46.040365, 'lng': 6.546846899999999}}, 'location': {'lat': 46.06039, 'lng': 6.580582}, 'location_type': 'APPROXIMATE', 'viewport': {'northeast': {'lat': 46.08459, 'lng': 6.608080999999999}, 'southwest': {'lat': 46.040365, 'lng': 6.546846899999999}}}, 'place_id': 'ChIJicNpE94GjEcRuiD-B6wY98Y', 'types': ['locality', 'political']}], 'status': 'OK'}

    class ResponseMocked:

        def __init__(self, status_code, data):
            self.status_code = status_code
            self.data = data

        def json(self):
            return self.data

    def mockreturn(request, stream=False):
        print('Mockreturn', request)
        return ResponseMocked(200, result_dct)

    monkeypatch.setattr(requests, 'get', mockreturn)
    assert script.gmaps_geocoding_request('cluses', 0) == result_dct


    #         location_dict = reply_dict['results'][0]['geometry']['location']
    #         # print(location_dict)

    #         gmaps_static_map_request(location_dict, key)

    #         geocoding_dict = reply_dict
    #     else:
    #         print('address not found')
    # else:
    #     print('google reply error')

    # del response

    # return geocoding_dict