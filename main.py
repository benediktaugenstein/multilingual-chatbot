import os
from flask import Flask

app = Flask(__name__)

print('hello')

@app.route('/')
def hello():
    return 'Hello World!'
