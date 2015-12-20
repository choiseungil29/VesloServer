#-*- coding: utf-8 -*-

from index import app

@app.route('/')
def main():
	return '형채형 바보!'