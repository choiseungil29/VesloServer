#-*- coding: utf-8 -*-

from flask import session

from index.urls import url
from index.urls import user
from index.urls import post

from index.models.user import User

from index import db_session

from sqlalchemy.orm.exc import NoResultFound

def existUserById(id):
    try:
        db_session.query(User).filter_by(id=id).one()
    except NoResultFound, e:
        return False
    return True

def existUserBySession(session):
    try:
        db_session.query(User).filter_by(session=session).one()
    except NoResultFound, e:
        return False
    return True