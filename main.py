import os
import sys
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

def helper(x):
    x=x.upper()
    return x

#@app.route('/')
def my_form():
    return render_template('input.html')

@app.route('/', methods=['POST'])
#@app.route('/')
def output():
    text = request.form['text']
    processed_text = helper(text)
    result = processed_text
    return render_template("input.html",result = result)
