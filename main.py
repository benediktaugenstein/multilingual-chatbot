import os
import sys
import numpy as np
from flask import Flask, render_template

app = Flask(__name__)

def helper(x):
    return x+1

@app.route('/')
def hello():
    test = helper(1)
    #print('Hello', file=sys.stdout)
    test2 = str(test)
    return test2
