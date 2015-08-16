from flask import request
from app import app

@app.route('/')
def index():
	return 'Hello World!'

@app.route('/uppercase', methods=['GET','POST'])
def uppercase():
	text = request.args.get('text', None, type=str)
	processed_text = text.upper()
	return processed_text
