import os
from flask import Flask
def test():
    print('test')

app = Flask(__name__)

@app.route('/')
def hello():
    test = 0
    test += 1
    print(test)
    return 'test'
