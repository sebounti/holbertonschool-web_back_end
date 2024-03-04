#!/usr/bin/python3
""" Module to start a Flask web application """
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Configuration for languages """
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)
Babel.default_locale = "en"
Babel.default_timezone = "UTC"


@app.route("/", methods=['GET'])
def index():
    """ route to display a message"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
