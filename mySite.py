import pickle
import numpy as np
from flask import Flask, request, render_template, jsonify, Response

app = Flask('myApp')

@app.route('/')

def home():
    return 'Welcome to Patrick\'s Whiskey Recommendation System'

@app.route('/form') 

def form():
   return render_template('wrform.html')


@app.route('/submit')

def submit():
    user_input = request.args

    









if __name__ == '__main__':
    app.run(debug=True)