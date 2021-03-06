#-*- coding: utf-8 -*-

import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__)
#app.secret_key = os.urandom(24) # Flask-Login secret key
app.secret_key = 'clogicVeslo'
app.logger.info('secret key ' + app.secret_key)
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://clogic:ok154288tmddlf@localhost/Veslo" # db uri
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://itnpxmghkouqge:DrNcaRJ86jmr4IwHi9NK3mzHfP@ec2-54-83-204-159.compute-1.amazonaws.com:5432/d5inl38ocf5nlu" # db server uri
app.config['UPLOAD_FOLDER'] = 'index/static/image'

import logging
from logging import StreamHandler
file_handler = StreamHandler()
file_handler.setLevel(logging.WARNING)
app.logger.addHandler(file_handler)

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

# import db table
from index.models import user
from index.models import meeting
from index.models import tag
    
db.create_all()

db_session = db.session()

# import urls
from index import urls

if __name__ == '__main__':
	app.run()