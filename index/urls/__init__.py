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
        query.one()
    except NoResultFound, e:
        return False
    return True

def isLogin(userId):
    if userId in session:
        return True
    return False