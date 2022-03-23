import os
import numpy as np
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    x = np.sum([1,2,3])
    a = int(1)
    b = int(2)
    c = a + b
    #y = str(x)
    test = str(c)
    return test
