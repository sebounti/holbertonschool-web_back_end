#!/usr/bin/env python3
"""Module to start a Flask web application."""
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Configuration for languages."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', methods=["GET"])
def hello_world():
    """
    Greeting.

    Return:
        Initial template html.
    """
    return render_template('5-index.html')


def get_user(user_id) -> dict:
    """
    Get user from request
    """
    user_id = request.args.get('login_as')
    try:
        user_id = int(user_id)
        if user_id in users:
            return users[user_id]
    except (ValueError, TypeError):
        pass
    return None


@app.before_request
def before_request():
    """
    Get user, if any and set it as a global on flask.g.user
    """
    g.locale = str(get_locale())


@babel.localeselector
def get_locale():
    """Locale language.

    Return:
        Best match to the language.
    """
    locale = request.args.get('locale')
    if locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
