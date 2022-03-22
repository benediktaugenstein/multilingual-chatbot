import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/output')
def hello():
    test1 = float(1)
    test2 = float(2)
    test3 = test1 + test2
    return test3
