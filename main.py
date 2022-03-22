import os
from flask import Flask
print('hello2')
app = Flask(__name__)

print('hello')

@app.route('/')
def hello():
    return 'Hello World!'
