#-*-coding: utf-8 -*-

from index import app
from index import db

from sqlalchemy.dialects import postgresql

import datetime

class Meeting(db.Model):

    __tablename__ = "Meeting"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column('username', db.String)
    describe = db.Column('describe', db.String) # 내용
    session = db.Column('session', db.String)
    
    origin = db.Column('origin', db.String) # 출발지
    origin_lat = db.Column('origin_lat', db.Float) # 좌표
    origin_long = db.Column('origin_long', db.Float)

    dest = db.Column('dest', db.String) # 목적지
    dest_lat = db.Column('dest_lat', db.Float) # 좌표
    dest_long = db.Column('dest_long', db.Float)

    departure_time = db.Column('departure_time', db.DateTime) # 출발시간
    arrival_time = db.Column('time', db.DateTime) # 소요시간 

    registered_on = db.Column('registered_on', db.DateTime, default=db.func.now()) # 등록일자

    likes = db.Column('like', postgresql.ARRAY(postgresql.TEXT))
    
    def __init__(self):
        self.likes = []

    def to_json(self):
        item = {}
        item['username'] = self.username
        item['id'] = self.id
        item['session'] = self.session
        item['origin'] = self.origin
        item['origin_lat'] = self.origin_lat
        item['origin_long'] = self.origin_long

        item['dest'] = self.dest
        item['dest_lat'] = self.dest_lat
        item['dest_long'] = self.dest_long

        item['departure_time'] = str(self.departure_time)
        item['arrival_time'] = str(self.arrival_time)
        item['registered_on'] = str(self.registered_on)
        item['describe'] = self.describe

        item['likes'] = self.likes
        return item






