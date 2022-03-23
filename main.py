import os
import sys
import numpy as np
from myfuncs import helper2
from flask import Flask, render_template, request
from flask_caching import Cache

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)

app.config.from_mapping(config)
cache = Cache(app)

test_var = '0'
cache.set("my_value", test_var)

y = 'test'

def helper():
    my_value = cache.get("my_value")
    test_var_float = int(my_value)
    test_var_float += 1
    my_value = str(test_var_float)
    cache.set("my_value", my_value)
    return my_value

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

if __name__ == '__main__':
    app.run(threaded=False)
