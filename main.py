import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/output')
def hello():
    a = int(input(“Enter first number:”))
    b = int(input(“Enter second number:”))
    c = a + b
    return 'Hello'
