#!/usr/bin/env python3
"""Flask app for i18n and l10n."""

from flask import Flask, render_template


app = Flask(__name__)
application = app


@app.route("/", methods=["GET"])
def index():
    """Entry route."""
    return render_template("0-index.html")


if __name__ == "__main__":
    application.run(debug=True)
