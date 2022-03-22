import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    a = int(1)
    b = int(2)
    c = a + b
    test = str(c)
    return test
