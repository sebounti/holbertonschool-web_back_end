#!/usr/bin/env python3
"""Module to start a Flask web application."""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configuration for languages."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route('/', methods=["GET"])
def hello_world() -> str:
    """
    Greeting.

    Return:
        Initial template html.
    """
    return render_template('5-index.html', user=g.user)


@babel.localeselector
def get_locale() -> str:
    """Locale language.

    Return:
        Best match to the language.
    """
    locale = request.args.get('locale')
    if locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


def get_user(user) -> dict:
    """
    Get user from request
    """
    if user and dict(user) in users:
        return users.get(dict(user))


@app.before_request
def before_request():
    """
    Get user, if any
    """
    g.user = get_user(request.args.get('login_as'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
