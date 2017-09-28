import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))


DEBUG = True
# variable for debug tool bar working
SECRET_KEY = 'donguyenha'

REMEMBER_COOKIE_DURATION = timedelta(days=90)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
