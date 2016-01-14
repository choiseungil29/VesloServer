#-*- coding: utf-8 -*-

from index import db
from index import app

import datetime

class User(db.Model):

    __tablename__ = "User"

    id = db.Column('id', db.String, primary_key=True)
    username = db.Column('username', db.String)
    password = db.Column('password', db.String, nullable=True)
    type = db.Column('type', db.String)
    registered_on = db.Column('registered_on', db.DateTime, default=db.func.now())

    def __init__(self):
        self.password = None

    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)

    def to_json(self):
        item = {}
        item['id'] = self.id
        item['username'] = self.username
        item['type'] = self.type
        item['registered_on'] = str(self.registered_on)
        return item