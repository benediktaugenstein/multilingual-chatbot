import os
import sys
import numpy as np
from myfuncs import helper2
from flask import Flask, render_template, request, session
#from flask.ext.session import Session

app = Flask(__name__)

#SESSION_TYPE = 'filesystem'
#app.config.from_object(__name__)
#Session(app)

y = 'test'

def helper():
    return 'Hello'

@app.route('/')
def my_form():
    if not 'counter' in session:
        session['counter'] = 0
    session['counter'] += 1
    test_var_int = session['counter']
    test_var = str(test_var_int)
    return render_template('input.html')

@app.route('/', methods=['POST'])
#@app.route('/')
def output():
    text = request.form['text']
    processed_text = helper2(text)
    result = test_var + processed_text
    return render_template("input.html",result = result)

if __name__ == '__main__':
    app.run()
