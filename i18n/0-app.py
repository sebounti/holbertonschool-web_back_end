#!/usr/bin/python3
""" Module to start a Flask web application """
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    """ route to display a message"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
