#-*- coding: utf-8 -*-

import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__)
app.secret_key = 'Velslook154288tmddlf' # Flask-Login secret key
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://clogic:ok154288tmddlf@localhost/Veslo" # db uri

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

# import db table
from index.models import user

db.create_all()
session = db.session()

# import urls
from index import urls

if __name__ == '__main__':
	app.run