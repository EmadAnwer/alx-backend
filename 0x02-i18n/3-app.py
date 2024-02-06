#!/usr/bin/env python3
"""
3-app.py
"""

from flask import Flask, render_template
from flask_babel import Babel, _
from flask import request


class Config(object):
    """Config class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)


app.config.from_object(Config)


def get_locale():
    """Get locale from request"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get locale from request"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def hello_world() -> str:
    """Return a simple string as our response"""
    return render_template(
        "3-index.html", home_title=_("home_title"),
        home_header=_("home_header")
    )


if __name__ == "__main__":
    """Main"""
    app.run()
