#-*- coding: utf-8 -*-

import os

from index import app
from index import db_session

from index.models.user import User

from flask import request, session, redirect, url_for

import json
import index.urls

@app.route('/signup')
def signup():
    result = {}
    result['requestCode'] = 1
    result['requestMessage'] = 'success'
    return json.dumps(result, ensure_ascii=False)

@app.route('/login/kakao', methods=['GET'])
def login_kakao():
    result = {}

    id = request.args['id']
    username = request.args['username']

    if index.urls.isExistUser(id) == False:
        user = User()
        user.type = 'KAKAO'
        user.id = id
        user.username = username
        db_session.add(user)
        db_session.commit()

        app.logger.info('user : ' + str(user.to_json()))
        result['user'] = user.to_json()
    
    session[id] = user.id
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








