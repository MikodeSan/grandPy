import query as script


class TestQuery:

    def test_query(self):

        quote_lst = [
            "Salut GrandPy ! Est-ce que tu connais l'adresse d'{}",
            "Salut GrandPy ! Dis moi où se situe {}, j'aimerais bien y aller.",
            "Où est {} ?",
            "Où se trouve {}.",
            "Je cherche l'adresse de {}",
            "Je cherche {}",
            "Je cherche {}. Sais-tu où ça se trouve ?",
            "Aller à {}",
            "Aller au {}",
            "Aller chez {}",
            "Aller en {}",
            "Tu connais cette adresse: {} ?",
            "connais-tu ce lieu {} ?",
            "Connais-tu cet endroit {} ?, je cherche à y aller.",
            "connais-tu ce coin {} ? Je dois aller chez eux",
            # "connais-tu ce spot {} ?, Ca m'a l'air assez chouette.",
            "J'ai rendez-vous au {} et je cherche cette adresse",
            "J'ai rdv au {} et je cherche cette adresse",
            "Aller en {}",
            "{} sais-tu où ça se trouve ?",
            "{} sais-tu comment y aller ?",
            "{}"
            ]

        place_lst = [
            "Paris",
            "Cité la Meynard",
            "OpenClassrooms",
            "Prades-le-Lez",
            "Rue Alexandra David Neel, Pradres-le-Lez",
            "Place de la comédie",
            "Somfy, Cluses",
            ""
        ]

        # place_lst = [
        #     "Paris",
        #     "Samoëns",
        #     "Cluses",
        #     "Cité la Meynard",
        #     "OpenClassrooms",
        #     "Prades-le-Lez",
        #     "Rue Alexandra David Neel, Pradres-le-Lez",
        #     "Montpellier",
        #     "Comédie",
        #     "Place de la comédie"
        #     "Tour lumina",
        #     "Japon",
        #     "MIT",
        #     "Awox",
        #     "Vivaltis",
        #     "Somfy, Cluses",
        #     ""
        # ]

        for quote in quote_lst:

            # print("quote:", quote)

            for place in place_lst:
                # print("place:", place)
                qt = quote.format(place)
                print("quote:", qt)

                query = script.ZQuery(qt)

                # define expected place
                place = query.remove_punctuation(place.lower())

                word_lst = place.split()
                place = ''.join([w + " " for w in word_lst if w not in query._STOP_WORD_FR_LIST_])
                if place not in ["", " ", "  ", "   "]:
                    while place[0] == " ":
                        place = place[1:]
                    while place[-1] == " ":
                        place = place[:-1]

                assert query.spot[0] == place

    # def test_latitude_degrees_range():
    #     with pytest.raises(AssertionError):
    #     position = script.Position(100, 100)
