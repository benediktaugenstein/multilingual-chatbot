import os
import sys
#import tensorflow as tf
#from tensorflow import keras
#from tensorflow.keras.preprocessing.text import Tokenizer
#from tensorflow.keras.preprocessing.sequence import pad_sequences
from datetime import datetime, timezone, timedelta
#from sklearn.preprocessing import LabelBinarizer
import pandas as pd
from myfuncs import *
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key='test'

#from datapreparation import *

@app.route('/')
def my_form():
    return render_template('input.html')

@app.route('/', methods=['POST'])
#@app.route('/')
def output():
    """
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    
    test_var_int = session['counter']
    test_var = str(test_var_int)
    text = request.form['text']
    processed_text = helper2(text)
    result = test_var + processed_text
    """
    text = request.form['text']
    result = new_input(text)
    return render_template("input.html",result = result)

#if __name__ == '__main__':
    #app.run()
