import os
import sys
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

def helper(x):
    print(x)

@app.route('/')
def my_form():
    return render_template('input.html')

@app.route('/', methods=['POST'])
def output():
    helper('hallo')
    text = request.form['text']
    processed_text = text.upper()
    if result in locals():
        break
    else:
        result = ''
    result = result + processed_text
    return render_template("input.html",result = result)
