#-*- coding: utf-8 -*-

from index import app

@app.route('/')
def main():
	return 'Hello Veslo!'