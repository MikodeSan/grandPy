import gmaps as script

import requests


def test_geocoding_return(monkeypatch):

    geocoding_reply_dct = {'results': [{'address_components': [{'long_name': 'Cluses', 'short_name': 'Cluses', 'types': ['locality', 'political']}, {'long_name': 'Haute-Savoie', 'short_name': 'Haute-Savoie', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Auvergne-Rhône-Alpes', 'short_name': 'Auvergne-Rhône-Alpes', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}, {'long_name': '74300', 'short_name': '74300', 'types': ['postal_code']}], 'formatted_address': '74300 Cluses, France', 'geometry': {'bounds': {'northeast': {'lat': 46.08459, 'lng': 6.608080999999999}, 'southwest': {'lat': 46.040365, 'lng': 6.546846899999999}}, 'location': {'lat': 46.06039, 'lng': 6.580582}, 'location_type': 'APPROXIMATE', 'viewport': {'northeast': {'lat': 46.08459, 'lng': 6.608080999999999}, 'southwest': {'lat': 46.040365, 'lng': 6.546846899999999}}}, 'place_id': 'ChIJicNpE94GjEcRuiD-B6wY98Y', 'types': ['locality', 'political']}], 'status': 'OK'}
    result_dct = {'address': '74300 Cluses, France', 'location': {'lat': 46.06039, 'lng': 6.580582}}

    class ResponseMocked:

        def __init__(self, status_code, data):
            self.status_code = status_code
            self.data = data

        def json(self):
            return self.data

    def mockreturn(url):
        return ResponseMocked(200, geocoding_reply_dct)

    monkeypatch.setattr(requests, 'get', mockreturn)

    maps = script.ZGMaps(0)
    assert maps.geocoding_request('cluses') == result_dct


def test_geocoding_url(monkeypatch):

    key = "azertyuiop"
    result = "https://maps.googleapis.com/maps/api/staticmap?center=14.6332414%2C-61.03804399999999&zoom=15&size=240x240&maptype=roadmap&markers=color%3Ablue%7Clabel%3AP%7C14.6332414%2C-61.03804399999999&key={}".format(key)

    maps = script.ZGMaps(key)

    assert maps.static_map_request_url(14.6332414, -61.03804399999999) == result
