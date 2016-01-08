#-*- coding: utf-8 -*-

from index import db

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