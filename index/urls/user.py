#-*- coding: utf-8 -*-

from index import app
from index import db_session

from index.models.user import User

from flask import request, session

from sqlalchemy.orm.exc import NoResultFound

import json
import index.urls

@app.route('/signup')
def signup():
    return '회원가입에 성공하였습니다.'

# kakao id값이 넘어온다.
@app.route('/signup_with_login/kakao', methods=['GET', 'POST'])
def signup_with_login_kakao():
    result = {}

    id = request.args['id']
    username = request.args['username']

    result['id'] = id
    result['username'] = username

    print id
    print username

    if index.urls.isLogin(id):
        print '1'
        result['requestCode'] = 3
        result['requestMessage'] = 'already login'
        return json.dumps(result, ensure_ascii=False)

    if index.urls.isExistUser(id):
        print '2'
        result['requestCode'] = 2
        result['requestMessage'] = 'success login'
        session[id] = id
        return json.dumps(result, ensure_ascii=False)

    print '3'
    user = User()
    user.type = 'KAKAO'
    user.id = id
    user.username = username
    db_session.add(user)
    db_session.commit()

    print '4'
    result['requestCode'] = 1
    result['requestMessage'] = 'success signup'

    print '5'
    return json.dumps(result, ensure_ascii=False)











