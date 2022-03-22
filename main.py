import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    test = 1 + 1
    print(test)
