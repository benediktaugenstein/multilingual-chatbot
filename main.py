import os
from flask import Flask
def test():
    print('test')

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'
