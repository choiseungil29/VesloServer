#-*- coding: utf-8 -*-

from index import app
from index import db
from index import db_session

import json
import index.urls


@app.route('/reset')
def reset():
    db.drop_all()
    db.create_all()
    return 'clear'