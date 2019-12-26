import os
from sqlalchemy import create_engine


# import psycopg2
# conn_string = "host='localhost' dbname='my_database' user='postgres' password='secret'"
# conn = psycopg2.connect(conn_string)


# To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(24)])
SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"

FB_APP_ID = 2783332485018666


# Database initialization
if os.environ.get('DATABASE_URL'):
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
else:
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')


# default
#engine = create_engine('postgresql://scott:tiger@localhost/mydatabase')
# psycopg2 explicit default version
#engine = create_engine('postgresql+psycopg2://postgres:NoP@stGre23@localhost/lab_fb.db')
# pg8000
#engine = create_engine('postgresql+pg8000://scott:tiger@localhost/mydatabase')