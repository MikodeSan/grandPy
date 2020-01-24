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


_HELLO_ = ["Hello", "Salut", "Comment vas-tu", "Hooo"]

_NICK_NAME_ = ["mon poussin", "mon coeur", "mon petit marshmallow", "mon petit chou à la crème"]
_WELCOME_ = ["ravis de te revoir", "ça me fait tellement plaisir de te revoir", "ton grandpy est toujours heureux de te voir", ]
_PROPOSAL_ = ["quel endroit cherches-tu cette fois", "quel lieu souhaites-tu visiter cette fois-ci", "où souhaites-tu aller aujourd'hui"]

_INTERLOCUTION_ = ["Ho Hoo", "Ah oui ?", "Voyez-vous ça", "Hmmm", "Aaahh", "Oh très bien"]
# _INTERLOCUTION_ = ["Ho Hoo", "Ah oui ?", "Voyez-vous ça", "Hmmm", "Aaahh"]

_QUESTION_ = ["tu cherches", "tu veux savoir où se situe", "tu connais l'adresse de", "tu demandes où est"]

_EXCUSE_ = ["Houlala", "Aïe aïe aïe", "Excuse moi", "Hooo désolé"]
_EXCUSE_2_ = ["Je n'ai pas bien compris", "j'ai mal entendu", "j'ai dû loupé quelques mots", "je crois que je n'ai plus les oreilles de ma jeunesse"]
_REFORM_ = ["peux-tu reformuler ta question", "peux-tu reprendre plus simplement pour ton petit grand-py chéri", "où veux-tu aller", "redis moi ça s'il te plait", "plus doucement s'il te plait", "s'il te plait, parle moins vite"]
# _EXCUSE_ = ["Houlala", "Aïe Aïe", "Excuse moi", "Hooo Désolé"]
# _EXCUSE_ = ["Houlala", "Aïe Aïe", "Excuse moi", "Hooo Désolé"]


def zparse(query, key):

    place_lst = []

    qry = ZQuery(query)
    geocoding_dct = {}

    # extract specified place/spot from query
    place = qry.spot
    print("place: ", place)

    geocoding_dct['place'] = place
    is_understood = False

    if not place:
        geocoding_dct['reply'] = no_place()

    elif len(place) == 1:
        geocoding_dct['reply'] = defined_place(place[0])
        is_understood = True
    else:
        geocoding_dct['reply'] = many_place(place)


    if is_understood:

        # get place geocoding
        gmaps = ZGMaps(key)
        dct = gmaps.geocoding_request(place)
        print("geocode_dct: ", dct)

        if dct:

            geocoding_dct['address'] = dct['address']
            geocoding_dct['location'] = dct['location']

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


def welcome():

    hello = random.choice(_HELLO_)
    nick = random.choice(_NICK_NAME_)
    welcome = random.choice(_WELCOME_)
    proposal = random.choice(_PROPOSAL_)

    return hello + " " + nick + ", " + welcome + " ! " + proposal + " ?"


def no_place():

    excuse = random.choice(_EXCUSE_)
    nick = random.choice(_NICK_NAME_)
    n_excuse = random.choice(_EXCUSE_2_)
    reform = random.choice(_REFORM_)

    return excuse + " " + nick + ", " + n_excuse + " ... " + reform + " ?"


def defined_place(place):

    interloc = random.choice(_INTERLOCUTION_)
    nick = random.choice(_NICK_NAME_)
    question = random.choice(_QUESTION_)

    return interloc + " ! " + question + " ... " + place + " " + nick + " ?"


def many_place(_place_lst):

    excuse = random.choice(_EXCUSE_)
    nick = random.choice(_NICK_NAME_)
    n_excuse = random.choice(_EXCUSE_2_)
    proposal = random.choice(_PROPOSAL_)
    reform = random.choice(_REFORM_)

    s = excuse + " " + nick + ", " + n_excuse + ", " + reform + " ... " + proposal + " ? "

    for idx, place in enumerate(_place_lst):

        n = len(_place_lst) - 1
        if idx == n and n != 0:
            s += " ou "
        elif idx < n and idx != 0:
            s += ", "

        s += place

    return s


def parse():

    print("dummy for test")
    print("other dummy thing for test")
    pass


if __name__ == "__main__":

    gmaps_geocoding('cité la meynard', 'azerfghjkl51654mlkghfch')
