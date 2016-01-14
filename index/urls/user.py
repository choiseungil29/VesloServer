#-*- coding: utf-8 -*-

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

# kakao id값이 넘어온다.
@app.route('/signup/kakao', methods=['GET', 'POST'])
def signup_with_login_kakao():
    result = {}

    id = request.args['id']
    username = request.args['username']

    if index.urls.isExistUser(id):
        return redirect(url_for('login_kakao', id=id))

    user = User()
    user.type = 'KAKAO'
    user.id = id
    user.username = username
    db_session.add(user)
    db_session.commit()

    app.logger.info('user : ' + str(user.to_json()))
    result['user'] = user.to_json()

    result['requestCode'] = 1
    result['requestMessage'] = 'success signup'
    session[id] = user.id

    return json.dumps(result, ensure_ascii=False)

@app.route("/login/kakao", methods=['GET'])
def login_kakao():
    result = {}

    id = request.args['id']

    if index.urls.isExistUser(id) == False:
        result['requestCode'] = -1
        result['requestMessage'] = 'not exist user'
        return json.dumps(result, ensure_ascii=False)

    result['user'] = db_session.query(User).filter_by(id=id).one().to_json()

    if index.urls.isLogin(id):
        result['requestCode'] = 1
        result['requestMessage'] = 'already login'
        return json.dumps(result, ensure_ascii=False)

    session[id] = id
    result['requestCode'] = 1
    result['requestMessage'] = 'success login'
    result['session_id'] = session[id]
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








