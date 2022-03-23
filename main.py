import os
import sys
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

def helper(x):
    return x+1

@app.route('/', methods=['GET', 'POST'])
def output():
    if request.method == "POST":
       inp = request.form.get("inp") # name="inp" in html
       return "Your input is "+inp
    return render_template("output.html")
