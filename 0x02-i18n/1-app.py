#!/usr/bin/env python3
"""Flask app for i18n and l10n."""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
application = app
babel = Babel(app)


class Config(object):
    """Accepted languages."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/", methods=["GET"])
def index():
    """Entry route."""
    return render_template("1-index.html")


if __name__ == "__main__":
    application.run(debug=True)
