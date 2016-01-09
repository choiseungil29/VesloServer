#-*- coding: utf-8 -*-

from flask import session

from index.urls import url
from index.urls import user

from index.models.user import User

from index import db_session

from sqlalchemy.orm.exc import NoResultFound

def isExistUser(userId):
    query = db_session.query(User).filter_by(id=userId)
    try:
        print 'what'
        query.one()
    except NoResultFound, e:
        print 'what2'
        return False
    print 'what3'
    return True

def isLogin(userId):
    if userId in session:
        print 'what4'
        return True
    print 'what5'
    return False