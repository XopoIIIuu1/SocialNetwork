import os
from __init__ import app

CSRF_ENABLED = True
SECRET_KEY = 'djfbvkdfnjvnj239p[QqlkxmQLKMo2j340sdcjwd2'

basedir = os.path.abspath(os.path.dirname(__name__))
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.sqlite')
