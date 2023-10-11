#!/usr/bin/env python3

"""
Use the requests module to query
 your web server for the corresponding end-point.
  Use assert to validate the response expected
   status code and payload (if any) for each task.
"""

import requests

url = "http://localhost:5000/"


def register_user(email: str, password: str) -> None:
    """Register new user"""
    global url
    url += "users"
    payload = {"email": email, "password": password}

    response = requests.post(url, data=payload)
    assert response.status_code == 200


def log_in_wrong_password(email: str, password: str) -> None:
    """User enter wrong password while login"""
    global url
    url += "sessions"
    payload = {"email": email, "password": password}

    response = requests.post(url, data=payload)
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """User logs in successfully"""
    global url
    url += "sessions"
    payload = {"email": email, "password": password}

    response = requests.post(url, data=payload)
    # might needs cookies
    assert response.status_code == 200


def profile_unlogged() -> None:
    """Profil not accessible - User Unlogged"""
    global url
    url += "profile"
    response = requests.get(url)
    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """Profil accessible - User Logged"""
    global url
    url += "profile"
    payload = {"session_id": session_id}

    response = requests.get(url)
    assert response.status_code == 200


def log_out(session_id: str) -> None:
    """Logs out successfully"""
    global url
    url += "session"
    payload = {"session_id": session_id}

    response = requests.get(url, data=payload)
    assert response.status_code == 200


def reset_password_token(email: str) -> str:
    """Reset password - Get token"""
    global url
    url += "reset_password"
    payload = {"email": email}

    response = requests.post(url, data=payload)
    assert response.status_code == 200


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Update password - Using reset_token"""
    global url
    url += "reset_password"
    payload = {"email": email, "reset_token": reset_token,
               "new_password": new_password}

    response = requests.post(url, data=payload)

    assert response.status_code == 200


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
