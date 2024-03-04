#!/usr/bin/python3
""" Module to start a Flask web application """

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def hello_world():
    """  Function to handle requests to the root of the web app"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
