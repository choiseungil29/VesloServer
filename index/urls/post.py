#-*- coding: utf-8 -*-

from index import app
from index import db
from index import db_session

from index.models.user import User
from index.models.tag import Tag
from index.models.meeting import Meeting

from flask import request, session
from werkzeug import secure_filename

from sqlalchemy.orm.exc import NoResultFound

import json
import index.urls
import datetime

@app.route('/regist/meeting', methods=['POST'])
def regist_meeting():

    result = {}
    session = request.form['session']

    if index.urls.existUserBySession(session) == False:
        result['requestCode'] = -1
        result['requestMessage'] = '등록되지 않은 계정입니다.'
        return json.dumps(result, ensure_ascii=False)

    result['requestCode'] = 1
    result['requestMessage'] = '일정이 등록되었습니다.'

    post = Meeting()
    user = db_session.query(User).filter_by(session=session).one()
    post.username = user.username
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

    tags = [tag for tag in post.describe.split(' ') if tag.startswith('#')]
    for message in tags:
        query = db_session.query(Tag).filter_by(id=message)
        tag = None
        try:
            tag = query.one()
            tag.count += 1
        except NoResultFound, e:
            tag = Tag()
            tag.id = message
            tag.count = 1`
            db_session.add(tag)
        db_session.commit()

    db_session.add(post)
    db_session.commit()

    result['post'] = post.to_json()

    return json.dumps(result, ensure_ascii=True)

@app.route('/like/meeting', methods=['GET'])
def like_meeting():

    result = {}
    session = request.form['session']
    meeting_id = request.form['id']

    meeting = db_session.query(Post).filter_by(id=meeting_id).one()

    if session in meeting.likes:
        meeting.likes.remove(session)
    else:
        meeting.likes.append(session)

    result['requestCode'] = 1
    result['requestMessage'] = 'Success like or unlike'
    result['meeting'] = append.to_json()

    return json.dumps(result, ensure_ascii=False)

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

@app.route('/regist/post', methods=['POST'])
def regist_post():
    result = {}
    session = request.form['session']

    ALLOWD_EXTENSIONS = set(['jpg', 'jpeg', 'png', 'bmp'])

    file = request.files['resource']
    if file and allowed_file(file.filename):
        pass

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWD_EXTENSIONS






