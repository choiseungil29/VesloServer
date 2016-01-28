#-*- coding: utf-8 -*-

from index import db

user_meeting = db.Table('user_meeting',\
    db.Column('user_id', db.String, db.ForeignKey('User.id')),\
    db.Column('meeting_id', db.Integer, db.ForeignKey('Meeting.id')))

from index.models import user
from index.models import meeting
