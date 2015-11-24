#-*- coding: utf-8 -*-

from index import db

class User(db.Model):

    __tablename__ = "User"

    id = db.Column('id', db.String, primary_key=True)
    username = db.Column('username', db.String)
    password = db.Column('password', db.String)
    registered_on = db.Column('registered_on', db.DateTime)

    def __init__(self):
        pass

    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)