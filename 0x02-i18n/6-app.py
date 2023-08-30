#!/usr/bin/env python3
"""Flask app for i18n and l10n."""

from flask import Flask, render_template, request, g
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
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    elif g.user and g.user.get("locale"):
        locale = g.user.get("locale")
        return locale \
            if locale in app.config["LANGUAGES"] \
            else app.config["BABEL_DEFAULT_LOCALE"]
    elif request.accept_languages:
        return request.accept_languages.best_match(
            app.config["LANGUAGES"]
        )
    return app.config["BABEL_DEFAULT_LOCALE"]


def get_user():
    """Return active user."""
    uid = request.values.get("login_as")
    if uid:
        try:
            return users.get(int(uid))
        except Exception:
            return None
    return None


@app.before_request
def before_request():
    """To run befor request."""
    user = get_user()
    if user:
        g.user = user
    else:
        g.user = None


@app.route("/", methods=["GET"])
def index():
    """Entry route."""
    return render_template("6-index.html")


if __name__ == "__main__":
    application.run(debug=True)
