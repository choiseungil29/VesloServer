# -*- coding: utf-8 -*-

from index import app
from index import db

class Tag(db.Model):

    __tablename__ = 'Tag'

    id = db.Column(db.String, primary_key=True)
    count = db.Column(db.Integer)

    def __init__(self):
        pass

    def to_json(self):
        item = {}
        item['id'] = self.id
        item['count'] = self.count

        return item