import os
from flask import Flask
def test():
    print('test')

app = Flask(__name__)
test = 0
@app.route('/')
def hello():
    test += 1
    return 'Hello World!'
