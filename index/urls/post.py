#-*- coding: utf-8 -*-

from index import app
from index import db
from index import db_session

from index.models.user import User
from index.models.post import Post

from flask import request, session

import json
import index.urls
import datetime

@app.route('/post/meeting', methods=['POST'])
def post_meeting():

    result = {}

    session = request.form['session']

    if index.urls.existUserBySession(session) == False:
        result['requestCode'] = -1
        result['requestMessage'] = '등록되지 않은 계정입니다.'
        return json.dumps(result, ensure_ascii=False)

    result['requestCode'] = 1
    result['requestMessage'] = '일정이 등록되었습니다.'

    post = Post()
    user = db_session.query(User).filter_by(session=session).one()
    #post.writer_id = user.id
    post.session = user.session
    
    post.origin = request.form['origin']
    post.origin_lat = request.form['origin_lat']
    post.origin_long = request.form['origin_long']

    post.dest = request.form['dest']
    post.dest_lat = request.form['dest_lat']
    post.dest_long = request.form['dest_long']

    post.departure_time = datetime.datetime.fromtimestamp(int(request.form['departure_time'])/1000.0) # long to datetime 필요
    post.arrival_time = datetime.datetime.fromtimestamp(int(request.form['arrival_time'])/1000.0) # long to datetime 필요

    post.describe = request.form['describe']

    db_session.add(post)
    db_session.commit()

    result['post'] = post.to_json()

    return json.dumps(result, ensure_ascii=True)

@app.route('/post/meeting/all', methods=['POST'])
def get_all_meeting():

    result = {}
    session = request.form['session']

    if index.urls.existUserBySession(session) == False:
        result['requestCode'] = -1
        result['requestMessage'] = '등록되지 않은 계정입니다.'
        return json.dumps(result, ensure_ascii=False)        

    result['requestCode'] = 1
    result['requestMessage'] = '조회에 성공했습니다.'

    post_all = []

    query = db_session.query(Post).filter_by(session=session)
    post_all = query.all()

    result['meeting'] = []
    for post in post_all:
        result['meeting'].append(post.to_json())
        #app.logger.info('post ' + post.describe)

    return json.dumps(result)








