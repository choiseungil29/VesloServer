#-*-coding: utf-8 -*-

from index import app
from index import db

import datetime

class Post(db.Model):

    __tablename__ = "Post"

    id = db.Column(db.Integer, primary_key=True)
    describe = db.Column('describe', db.String) # 내용

    writer_id = db.Column('writer_id', db.String) # 작성자
    
    origin = db.Column('origin', db.String) # 출발지
    origin_lat = db.Column('origin_lat', db.Float) # 좌표
    origin_long = db.Column('origin_long', db.Float)

    dest = db.Column('dest', db.String) # 목적지
    dest_lat = db.Column('dest_lat', db.Float) # 좌표
    dest_long = db.Column('dest_long', db.Float)

    departure_time = db.Column('departure_time', db.DateTime) # 출발시간
    arrival_time = db.Column('time', db.DateTime) # 소요시간 

    registered_on = db.Column('registered_on', db.DateTime, default=db.func.now()) # 등록일자

    def __init__(self):
        pass