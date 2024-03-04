#!/usr/bin/env python3
""" Module to start a Flask web application """
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config(object):
    """ Configuration for languages """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__, template_folder='templates')
babel = Babel(app)
app.config.from_object(Config)


@app.route('/')
def index():
    """ route to display a message"""
    return render_template("1-index.html")


@babel.localeselector
def get_locale():
    """ Select a language translation """
    user_locale = request.args.get('locale')
    if user_locale in app.config['LANGUAGES']:
        return user_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=["GET"])
def hello_world():
    """
    index template
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
