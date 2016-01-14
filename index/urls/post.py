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

    if index.urls.isLogin(request.form.get('writer_id')) == False:
        result['requestCode'] = -1
        result['requestMessage'] = '로그인이 필요한 서비스입니다.'
        return json.dumps(result, ensure_ascii=False)

    result['requestCode'] = 1
    result['requestMessage'] = '일정이 등록되었습니다.'

    post = Post()
    post.writer_id = request.form['writer_id']
    
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

    result['post'] = {}
    result['post']['writer_id'] = post.writer_id
    result['post']['id'] = post.id
    result['post']['origin'] = post.origin
    result['post']['dest'] = post.dest

    return json.dumps(result, ensure_ascii=True)

@app.route('/post/meeting/all', methods=['POST'])
def get_all_meeting():

    result = {}
    id = request.form['id']

    app.logger.info('welcome')
    app.logger.info('id : ' + id)
    app.logger.info('session : ' + session[id])

    if index.urls.isLogin(id) == False:
        result['requestCode'] = -1
        result['requestMessage'] = '로그인이 필요한 서비스입니다.'
        return json.dumps(result, ensure_ascii=False)

    result['requestCode'] = 1
    result['requestMessage'] = '조회에 성공했습니다.'

    post_all = []

    query = db_session.query(Post).filter_by(writer_id=id)
    post_all = query.all()

    result['meeting'] = []
    for post in post_all:
        item = {}
        item['writer_id'] = post.writer_id
        item['origin'] = post.origin
        item['origin_lat'] = post.origin_lat
        item['origin_long'] = post.origin_long
        item['dest'] = post.dest
        item['dest_lat'] = post.dest_lat
        item['dest_long'] = post.dest_long
        item['departure_time'] = post.departure_time
        item['arrival_time'] = post.arrival_time
        item['registered_on'] = post.registered_on.microsecond # datetime to milliseconds
        item['describe'] = post.describe

        result['meeting'].append(item)
        #app.logger.info('post ' + post.describe)

    return json.dumps(result)








