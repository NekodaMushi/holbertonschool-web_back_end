#!/usr/bin/env python3

"""Basic Flask app"""

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
    """Config class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel.init_app(app)


@app.route("/", methods=["GET"])
def index():
    """Render html template"""
    return render_template("6-index.html")


@babel.localeselector
def get_locale():
    """Determine best match with supported language"""
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    if g.user:
        locale = g.user.get("locale")
        if locale and locale in app.config["LANGUAGES"]:
            return locale
    locale = request.headers.get("locale")
    if locale and locale in Config.LANGUAGES:
        return locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone():
    """Find appropriate time zone"""

    timezone = request.args.get("timezone")
    if timezone:
        return timezone

    if g.user:
        timezone = g.user.get("timezone")
        if timezone:
            return timezone

    return request.headers.get("timezone")


@app.before_request
def before_request():
    """
    before_request function
    """
    g.user = get_user()


def get_user():
    """
    get_user function
    """
    user_id = request.args.get("login_as")
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    else:
        return None


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
