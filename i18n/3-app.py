#!/usr/bin/env python3
""" Module to start a Flask web application """
from flask import Flask, render_template
from flask_babel import Babel, _
from flask import request

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Configuration for languages """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """ Locale language
        Return:
            Best match to the language
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=["GET"])
def hello_world() -> str:
    """
    greeting in the language of the user
        Return:
            Initial template html
    """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
