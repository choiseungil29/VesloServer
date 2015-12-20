#-*-coding: utf-8 -*-

from index import app

class Post(db.Model):

    __tablename__ = "Post"

    id = db.Column('id', db.String, primary_key=True)
    describe = db.Column('describe', db.String)
    writer = db.Column('writer', db.String)
    registered_on = db.Column('registered_on', db.DateTime)

    def __init__(self):
        pass