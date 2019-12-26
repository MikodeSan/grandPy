from flask import Flask, render_template, url_for, request, jsonify
import requests

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/')
@app.route('/index/')
def index():
    description = """
        Toi, tu sais comment utiliser la console ! Jamais à court d'idées pour réaliser ton objectif, tu es déterminé-e et persévérant-e. Tes amis disent d'ailleurs volontiers que tu as du caractère et que tu ne te laisses pas marcher sur les pieds. Un peu hacker sur les bords, tu aimes trouver des solutions à tout problème. N'aurais-tu pas un petit problème d'autorité ? ;-)
    """
    return render_template('index.html')
                            # user_name='Julio',
                            # user_image=url_for('static', filename='img/profile.png'),
                            # description=description,
                            # blur=True)

@app.route('/zapp/', methods=['GET', 'POST'])
def zapp():

    # content = request.json
    # print(content)

    # data = request.get_json()
    # print(data)

    # data = request.form
    # print(data)

    user_name = request.args.get('user_name')
    # user_name = data.get('strUserQuery')

    return render_template('zapp.html',
                            user_name=user_name)


@app.route('/content/', methods=['GET', 'POST'])
def content():

    data = request.form
    print(data['query_text'])

    address_url = 'https://maps.googleapis.com/maps/api/geocode/json?address=place+de+la+coméde&key=AIzaSyAvVZSBIzuKvUREct8yRbmIAUJI2Ii_b3k'

    response = requests.get(address_url)
    if response.status_code == 200:
        address_dict = response.json()
        if address_dict['results'] and address_dict['status'] == "OK":
            data = address_dict['results'][0]
            # print(data['formatted_address'] + " " + data['geometry']['location']['lat'] + data['geometry']['location']['lng'])
            print(data['formatted_address'])
        else:
            print('address not found')
    else:
        print('google reply error')

    return address_dict

    # return jsonify(data)
    # return render_template('index.html')

    # return jsonify(data)


@app.route('/contents/<content_id>/')
def contents(content_id):
    # return '%s' % content_id
    return jsonify({'foo':"tutu"})


if __name__ == "__main__":
    app.run()
