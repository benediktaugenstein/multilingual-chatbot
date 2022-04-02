import os
import sys
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from datetime import datetime, timezone, timedelta
from sklearn.preprocessing import LabelBinarizer
import pandas as pd
from myfuncs import *
from flask import Flask, render_template, request, session

app = Flask(__name__)

model = keras.models.load_model('model/general/general.h5')
model2 = keras.models.load_model('model/feeling/feeling.h5')
link_general = 'data/general.csv'
link_feeling = 'data/feeling.csv'
models = [model, model2]
datasets = [link_general, link_feeling]
tokenizers = []
word_indices = []
sequences_array = []
lengths_input = []
labels_transformed_array = []

for i, model in enumerate(models):
  data = pd.read_csv(datasets[i])

  sentences = data['Sentence']
  labels = data['Result']

  #tokenizer = Tokenizer(num_words = 100)
  tokenizer = Tokenizer()
  tokenizer.fit_on_texts(sentences)
  word_index = tokenizer.word_index
  sequences = tokenizer.texts_to_sequences(sentences)

  tokenizers.append(tokenizer)
  word_indices.append(word_index)

  sequences = pad_sequences(sequences, padding='post', truncating='post')
  sequences_array.append(sequences)

  #word_count = len(word_index)
  len_input = len(sequences[0])
  lengths_input.append(len_input)
  if i == 0: # General
    ohe = LabelBinarizer()
    labels_transformed_general = ohe.fit_transform(labels)
  else: # Feeling
    ohe2 = LabelBinarizer()
    labels_transformed_feeling = ohe2.fit_transform(labels)
  #len_output = len(labels_transformed[0])

app.secret_key='test'

test = 'test123'

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
    result = new_input(text, tokenizers, lengths_input, models, ohe, ohe2)
    if 'fin_output' in session:
      session['fin_output'] = result + session['fin_output']
    else:
      session['fin_output'] = initial_input + '<br>' + output
    #var = text + test
    var = session['fin_output']
    result = str(var)
    return render_template("input.html",result = result)

#if __name__ == '__main__':
    #app.run()
