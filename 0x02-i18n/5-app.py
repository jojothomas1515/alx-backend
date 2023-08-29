#!/usr/bin/env python3
"""Flask app for i18n and l10n."""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
application = app
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Accepted languages."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Get the locale that is best matched."""
    locale = request.values.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(
        app.config["LANGUAGES"]
    )


def get_user():
    """Return active user."""
    uid = request.values.get("login_as")
    return users.get(uid)

@app.before_request
def before_request

@app.route("/", methods=["GET"])
def index():
    """Entry route."""
    return render_template("5-index.html")


if __name__ == "__main__":
    application.run(debug=True)
