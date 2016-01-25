#-*- coding: utf-8 -*-

from index import app
from index import db
from index import db_session

import json
import index.urls

@app.route('/reset')
def reset():
    app.logger.info('1')
    db.drop_all()
    app.logger.info('2')
    db.create_all()
    app.logger.info('3')
    return 'clear'