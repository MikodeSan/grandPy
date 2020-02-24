import os
from flask import url_for
from sqlalchemy import create_engine

import param

# import psycopg2
# conn_string = "host='localhost' dbname='my_database' user='postgres' password='secret'"
# conn = psycopg2.connect(conn_string)

ZPARSER_URI = 'parse'

# production environment
# Database initialization
if os.environ.get('DATABASE_URL'):
    # ZSERVER_URL = "http://z-grand-py.herokuapp.com"

    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

    GMAPS_KEY = os.environ['GMAPS_KEY']
    FONTAWESOME_ID = os.environ['FONTAWESOME_ID']


# dev environment
else:
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

    SECRET_KEY = param.SECRET_KEY

    GMAPS_KEY = param.GMAPS_KEY
    FB_APP_ID = param.FB_APP_ID
    FONTAWESOME_ID = param.FONTAWESOME_ID

# default
# engine = create_engine('postgresql://scott:tiger@localhost/mydatabase')
# psycopg2 explicit default version
# engine = create_engine('postgresql+psycopg2://postgres:NoP@stGre23@localhost/lab_fb.db')
# pg8000
# engine = create_engine('postgresql+pg8000://scott:tiger@localhost/mydatabase')
