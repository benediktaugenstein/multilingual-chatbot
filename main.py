import os
import sys
import numpy as np
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    x = np.array([1,2,3])
    a = int(1)
    b = int(2)
    c = a + b
    y = str(x)
    print('Hello', file=sys.stdout)
    test = str(c)
    return y
