#!/usr/bin/env python3

"""Basic flask app"""

from flask import Flask, jsonify, request, make_response, abort, redirect
from auth import Auth

app = Flask(__name__)


AUTH = Auth()


@app.route("/", methods=["GET"])
def basic():
    """Fn testing flask app"""
    return jsonify({"message": "Bienvenue"})


@app.route("/profile", methods=["GET"])
def profile():
    """Get access to user profil"""
    session_id = request.cookies.get("session_id")
    if session_id:
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            return jsonify({"email": user.email}), 200
    else:
        abort(403)


@app.route("/reset_password", methods=["POST"])
def get_reset_password_token():
    """Get reset token"""
    email = request.form.get("email")
    # if email:
    #     reset_token = AUTH.get_reset_password_token(email)
    #     if reset_token:
    #         return (
    #             jsonify({"email": email, "reset_token": reset_token}),
    #             200,
    #         )
    # else:
    #     abort(403)
    try:
        reset_token = AUTH.get_reset_password_token(email)
    except Exception:
        abort(403)
    return (
        jsonify({"email": email, "reset_token": reset_token}),
        200,
    )


@app.route("/reset_password", methods=["PUT"])
def update_password():
    """Updating password"""
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")

    try:
        password = AUTH.update_password(reset_token, new_password)
    except Exception:
        abort(403)
    return jsonify({"email": email, "message": "Password updated"}), 200


@app.route("/users", methods=["POST"])
def users():
    """Create new user"""
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"])
def login():
    """Log in User"""
    email = request.form.get("email")
    password = request.form.get("password")

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = make_response(
            jsonify({"email": "<user email>", "message": "logged in"})
        )
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)


@app.route("/sessions", methods=["DELETE"])
def logout():
    """Log out User"""
    session_id = request.cookies.get("session_id")
    if session_id:
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            AUTH.destroy_session(user.id)
            response = redirect("/")
            response.delete_cookie("session_id")
            return response
        else:
            abort(403)
    # try:
    #     user = AUTH.get_user_from_session_id(session_id)
    # except Exception:
    #     abort(403)
    # AUTH.destroy_session(user.id)
    # response = redirect("/")
    # response.delete_cookie("session_id")
    # return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
