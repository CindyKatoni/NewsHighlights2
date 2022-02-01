from flask import render_template
from app import app

import requests
import json
import os

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    req = requests.get('https://newsapi.org/v2/everything?q=bitcoin&apiKey={}'.format(os.environ.get("NEWS_API_KEY")))
    data = json.loads(req.content)['articles'][0]
    return render_template('index.html', data=data)

@app.route('/news', methods=['GET'])
def allnews():
    req = requests.get('https://newsapi.org/v2/everything?q=bitcoin&apiKey={}'.format(os.environ.get("NEWS_API_KEY")))
    data = json.loads(req.content)
    return render_template('allnews.html', data=data['articles'])



