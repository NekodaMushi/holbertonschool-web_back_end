#!/usr/bin/env python3

"""Basic flask app"""

from flask import Flask, jsonify, request, make_response, abort
from auth import Auth

app = Flask(__name__)


AUTH = Auth()


@app.route("/", methods=["GET"])
def basic():
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users():
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    if AUTH.valid_login(email, password) == True:
        session_id = AUTH.create_session(email)
        response = make_response(
            jsonify({"email": "<user email>", "message": "logged in"})
        )
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)

    # try:
    #     user = AUTH.valid_login(email, password)
    #     return jsonify({"email": email, "password": password, "message": "are correct"})
    # except


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
