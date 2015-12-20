#-*- coding: utf-8 -*-

from index import app

from flask import request

@app.route('/signup/<type>')
def signup(type):
    return '회원가입에 성공하였습니다. : ' + type

@app.route('/signup/kakao')
def signup_kakao():
    return 'kakao'