import string


class ZQuery:

    _STOP_WORD_FR_LIST_ = ["a","abord","absolument","afin","ah","ai","aie","ailleurs","ainsi","ait","allaient","allo","allons","allô","alors","anterieur","anterieure","anterieures","apres","après","as","assez","attendu","au","aucun","aucune","aujourd","aujourd'hui","aupres","auquel","aura","auraient","aurait","auront","aussi","autre","autrefois","autrement","autres","autrui","aux","auxquelles","auxquels","avaient","avais","avait","avant","avec","avoir","avons","ayant","b","bah","bas","basee","bat","beau","beaucoup","bien","bigre","boum","bravo","brrr","c","car","ce","ceci","cela","celle","celle-ci","celle-là","celles","celles-ci","celles-là","celui","celui-ci","celui-là","cent","cependant","certain","certaine","certaines","certains","certes","ces","cet","cette","ceux","ceux-ci","ceux-là","chacun","chacune","chaque","cher","chers","chez","chiche","chut","chère","chères","ci","cinq","cinquantaine","cinquante","cinquantième","cinquième","clac","clic","combien","comme","comment","comparable","comparables","compris","concernant","contre","couic","crac","d","da","dans","de","debout","dedans","dehors","deja","delà","depuis","dernier","derniere","derriere","derrière","des","desormais","desquelles","desquels","dessous","dessus","deux","deuxième","deuxièmement","devant","devers","devra","different","differentes","differents","différent","différente","différentes","différents","dire","directe","directement","dit","dite","dits","divers","diverse","diverses","dix","dix-huit","dix-neuf","dix-sept","dixième","doit","doivent","donc","dont","douze","douzième","dring","du","duquel","durant","dès","désormais","e","effet","egale","egalement","egales","eh","elle","elle-même","elles","elles-mêmes","en","encore","enfin","entre","envers","environ","es","est","et","etant","etc","etre","eu","euh","eux","eux-mêmes","exactement","excepté","extenso","exterieur","f","fais","faisaient","faisant","fait","façon","feront","fi","flac","floc","font","g","gens","h","ha","hein","hem","hep","hi","ho","holà","hop","hormis","hors","hou","houp","hue","hui","huit","huitième","hum","hurrah","hé","hélas","i","il","ils","importe","j","je","jusqu","jusque","juste","k","l","la","laisser","laquelle","las","le","lequel","les","lesquelles","lesquels","leur","leurs","longtemps","lors","lorsque","lui","lui-meme","lui-même","là","lès","m","ma","maint","maintenant","mais","malgre","malgré","maximale","me","meme","memes","merci","mes","mien","mienne","miennes","miens","mille","mince","minimale","moi","moi-meme","moi-même","moindres","moins","mon","moyennant","multiple","multiples","même","mêmes","n","na","naturel","naturelle","naturelles","ne","neanmoins","necessaire","necessairement","neuf","neuvième","ni","nombreuses","nombreux","non","nos","notamment","notre","nous","nous-mêmes","nouveau","nul","néanmoins","nôtre","nôtres","o","oh","ohé","ollé","olé","on","ont","onze","onzième","ore","ou","ouf","ouias","oust","ouste","outre","ouvert","ouverte","ouverts","o|","où","p","paf","pan","par","parce","parfois","parle","parlent","parler","parmi","parseme","partant","particulier","particulière","particulièrement","pas","passé","pendant","pense","permet","personne","peu","peut","peuvent","peux","pff","pfft","pfut","pif","pire","plein","plouf","plus","plusieurs","plutôt","possessif","possessifs","possible","possibles","pouah","pour","pourquoi","pourrais","pourrait","pouvait","prealable","precisement","premier","première","premièrement","pres","probable","probante","procedant","proche","près","psitt","pu","puis","puisque","pur","pure","q","qu","quand","quant","quant-à-soi","quanta","quarante","quatorze","quatre","quatre-vingt","quatrième","quatrièmement","que","quel","quelconque","quelle","quelles","quelqu'un","quelque","quelques","quels","qui","quiconque","quinze","quoi","quoique","r","rare","rarement","rares","relative","relativement","remarquable","rend","rendre","restant","reste","restent","restrictif","retour","revoici","revoilà","rien","s","sa","sacrebleu","sait","sans","sapristi","sauf","se","sein","seize","selon","semblable","semblaient","semble","semblent","sent","sept","septième","sera","seraient","serait","seront","ses","seul","seule","seulement","si","sien","sienne","siennes","siens","sinon","six","sixième","soi","soi-même","soit","soixante","son","sont","sous","souvent","specifique","specifiques","speculatif","stop","strictement","subtiles","suffisant","suffisante","suffit","suis","suit","suivant","suivante","suivantes","suivants","suivre","superpose","sur","surtout","t","ta","tac","tant","tardive","te","tel","telle","tellement","telles","tels","tenant","tend","tenir","tente","tes","tic","tien","tienne","tiennes","tiens","toc","toi","toi-même","ton","touchant","toujours","tous","tout","toute","toutefois","toutes","treize","trente","tres","trois","troisième","troisièmement","trop","très","tsoin","tsouin","tu","té","u","un","une","unes","uniformement","unique","uniques","uns","v","va","vais","vas","vers","via","vif","vifs","vingt","vivat","vive","vives","vlan","voici","voilà","vont","vos","votre","vous","vous-mêmes","vu","vé","vôtre","vôtres","w","x","y","z","zut","à","â","ça","ès","étaient","étais","était","étant","été","être","ô"]
    _STOP_WORD_ADDR_FR_LIST_ = ["adresse","situe","situé","située","où est","ou est","trouve","trouvé","cherche","aller","allé","lieu","endroit","coin","spot","connais","connaissez","rendez-vous","rdv", "!", ".", "?", "salut", "hello", "grandpy","grand-père", "papi", "papy", "dis", "aimerais", "sais", "dois", "donne"]


    def __init__(self, _query):

        self.quote = _query.lower()

        self.spot = self.extract_place()

    def extract_place(self):

        spot = ""

        # Replace address stop word by defined separator
        separator = "§"
        quote = self.quote
        # print("Quote:", quote)

        for w in self._STOP_WORD_ADDR_FR_LIST_:
            
            quote = quote.replace(w, separator)

        # print("Quote - stop word:", quote)
        
        # Replace punctuation by space
        quote = self.remove_punctuation(quote)
        # print("Quote - punctuation:", quote)

        # Remove stopwords
        word_lst = quote.split();

        quote = ''.join([w + " " for w in word_lst if w not in self._STOP_WORD_FR_LIST_] )
        # print("Quote - stop word:", quote)

        # Remove separator
        word_lst = quote.split(separator);
        # print("word_lst:", word_lst)
        address_lst = []
        for w in word_lst:
            
            if w not in ["", " ", "  ", "   "]:
                while w[0] == " ":
                    w = w[1:]
                while w[-1] == " ":
                    w = w[:-1]
                
                address_lst.append(w)
                # print(address_lst)

        if not address_lst:
            address_lst = [""]

        print("extracted spot:", address_lst, "\n")

        return address_lst

        # Find address part from quote 

        # if len(strdata) > 1:

        #     print(strdata)

        #     spot = strdata[1]
        #     print("Query address:", spot)

        #     # Replace punctuation by space
        #     self.remove_punctuation(spot)
            
        #     print("Final spot", spot);

        # return spot

    # def extract_place(self):

    #     spot = ""

    #     # Find address part from quote 
    #     self.quote

    #     # spot = self.quote


    #     # # Remove stopwords
    #     # word_lst = spot.split();
    #     # print("Split", word_lst)

    #     # spot = ''.join([w + " " for w in word_lst if w not in self._STOP_WORD_FR_LIST_] )
    #     # print(spot)

    #     strdata = self.quote.split("adresse ", 1)

    #     if len(strdata) > 1:

    #         print(strdata)

    #         spot = strdata[1]
    #         print("Query address:", spot)

    #         # Replace punctuation by space
    #         self.remove_punctuation(spot)
    
    #         # print("Punctuation", string.punctuation)
    #         # exclude = set(string.punctuation)
    #         # spot = ''.join(ch if ch not in exclude else " " for ch in spot)

    #         # if spot[-1] == " ":
    #         #     spot.pop()            
                
    #         # Remove stopwords
    #         word_lst = spot.split();
    #         print("Split", word_lst)

    #         print("Final spot", spot);

    #         ## Some alternative examples
    #         ### 1.
    #         # s.translate(None, string.punctuation)
    #         ### 2.
    #         # s.translate(str.maketrans('', '', string.punctuation))
    #         ### 3. translate is the best
    #         # import re, string, timeit

    #         # s = "string. With. Punctuation"
    #         # exclude = set(string.punctuation)
    #         # table = string.maketrans("","")
    #         # regex = re.compile('[%s]' % re.escape(string.punctuation))

    #         # def test_set(s):
    #         #     return ''.join(ch for ch in s if ch not in exclude)

    #         # def test_re(s):  # From Vinko's solution, with fix.
    #         #     return regex.sub('', s)

    #         # def test_trans(s):
    #         #     return s.translate(table, string.punctuation)

    #         # def test_repl(s):  # From S.Lott's solution
    #         #     for c in string.punctuation:
    #         #         s=s.replace(c,"")
    #         #     return s

    #         # print "sets      :",timeit.Timer('f(s)', 'from __main__ import s,test_set as f').timeit(1000000)
    #         # print "regex     :",timeit.Timer('f(s)', 'from __main__ import s,test_re as f').timeit(1000000)
    #         # print "translate :",timeit.Timer('f(s)', 'from __main__ import s,test_trans as f').timeit(1000000)
    #         # print "replace   :",timeit.Timer('f(s)', 'from __main__ import s,test_repl as f').timeit(1000000)

    #     return spot

    def remove_punctuation(self, _str, _char=" "):
        # Replace punctuation by space
        # print("Punctuation", string.punctuation)
        exclude = set(string.punctuation)
        quote = ''.join(ch if ch not in exclude else _char for ch in _str)

        # print("test quote", quote, type(quote))
        if quote and quote[-1] == _char:
            quote = quote[:-1]

        return quote


if __name__ == "__main__":
    query = ZQuery()
    print(query.quote)
