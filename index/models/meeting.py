#-*-coding: utf-8 -*-

from index import app

class Meeting(db.Model):

    __tablename__ = 'Meeting'

    id = db.Column('id', db.String, primary_key=True)
    name = db.Column('name', db.String) # 모임 이름
    meet_date = db.Column('meet_name', db.DateTime)
    
