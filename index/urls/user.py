#-*- coding: utf-8 -*-

import os

from index import app
from index import db_session

from index.models.user import User

from flask import request, session, redirect, url_for

from sqlalchemy.orm.exc import NoResultFound

import json
import index.urls

@app.route('/login/kakao', methods=['GET'])
def login_kakao():
    result = {}

    id = request.args['id']
    username = request.args['username']
    profile_path = request.args['profile_path']

    if index.urls.existUserById(id) == False:
        user = User()
        user.type = 'KAKAO'
        user.id = id
        user.username = username
        user.profile_img_url = profile_path
        db_session.add(user)
        db_session.commit()

        result['user'] = user.to_json()
        return json.dumps(result, ensure_ascii=False)
    
    user = db_session.query(User).filter_by(id=id).one()
    result['user'] = user.to_json()
    result['requestCode'] = 1
    result['requestMessage'] = 'success login'
    return json.dumps(result, ensure_ascii=False)

@app.route('/get/user/all', methods=['GET'])
def getAllUsers():
    result = {}

    users = db_session.query(User).all()

    result['users'] = []
    for user in users:
        item = user.to_json()
        result['users'].append(item)

    return json.dumps(result)

@app.route('/session/validate', methods=['POST'])
def validateSession():
    result = {}

    session = request.form['session']
    app.logger.info('session : ' + session)

    if index.urls.existUserBySession(session) == False:
        result['requestCode'] = -1
        result['requestMessage'] = 'invalidate session'
        result['errorSession'] = session
        return json.dumps(result)

    result['requestCode'] = 1
    result['requestMessage'] = 'validate session'
    return json.dumps(result)






