import query as script


class TestQuery:

    def test_query(self):
        query = script.ZQuery()

        assert query.quote == "Default quote"

    def test_extract_place(self):

        query = script.ZQuery()

        quote = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"

        spot = query.extract_place(quote)

        assert spot == "OpenClassrooms"

    # def test_latitude_degrees_range():
    #     with pytest.raises(AssertionError):
    #     position = script.Position(100, 100)
