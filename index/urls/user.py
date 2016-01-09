#-*- coding: utf-8 -*-

from index import app
from index import db_session

from index.models.user import User

from flask import request, session

import json
import index.urls

@app.route('/signup')
def signup():
    result = {}
    result['requestCode'] = 1
    result['requestMessage'] = 'success'
    return json.dumps(result, ensure_ascii=False)

# kakao id값이 넘어온다.
@app.route('/signup_with_login/kakao', methods=['GET', 'POST'])
def signup_with_login_kakao():
    result = {}

    id = request.args['id']
    username = request.args['username']

    result['user'] = {}
    result['user']['id'] = id
    result['user']['username'] = username

    if index.urls.isLogin(id):
        result['requestCode'] = 3
        result['requestMessage'] = 'already login'
        return json.dumps(result, ensure_ascii=False)

    if index.urls.isExistUser(id):
        result['requestCode'] = 2
        result['requestMessage'] = 'success login'
        session[id] = id
        result['session_id'] = session[id]
        return json.dumps(result, ensure_ascii=False)

    user = User()
    user.type = 'KAKAO'
    user.id = id
    user.username = username
    db_session.add(user)
    db_session.commit()

    result['requestCode'] = 1
    result['requestMessage'] = 'success signup'

    return json.dumps(result, ensure_ascii=False)











