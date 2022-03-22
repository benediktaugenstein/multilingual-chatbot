import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/output')
def hello():
    test = 1+1
    return render_template('output.html', entry=output)

def test():
    return 'Hello World!'
    
test = test()
