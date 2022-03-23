import os
import sys
import numpy as np
from myfuncs import helper2
from flask import Flask, render_template, request
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.run(threaded=True)

test_var = '0'
y = 'test'

def helper():
    global test_var
    test_var_float = int(test_var)
    test_var_float += 1
    test_var = str(test_var_float)
    return test_var

@app.route('/')
def my_form():
    return render_template('input.html')

@app.route('/', methods=['POST'])
#@app.route('/')
def output():
    text = request.form['text']
    processed_text = helper2(text)
    more_text = helper()
    result = more_text + processed_text
    return render_template("input.html",result = result)
