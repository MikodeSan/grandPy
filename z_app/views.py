from flask import Flask, render_template, url_for, request, jsonify

import requests

from .zmodel import grandPy


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

@app.route('/zapp/', methods=['GET', 'POST'])
def zapp():

    user_name = request.args.get('user_name')

    _welcome = grandPy.welcome()

    return render_template('zapp.html',
                            user_name=user_name,
                            isApp=True,
                            welcome=_welcome)


@app.route('/parse/', methods=['GET', 'POST'])
def parse():

    data = request.form
    query = data['query_text']

    # set url
    return grandPy.zparse(query, app.config['GMAPS_KEY'])

@app.route('/contents/<content_id>/')
def contents(content_id):
    return jsonify({'foo':"tutu"})


if __name__ == "__main__":
    app.run()
