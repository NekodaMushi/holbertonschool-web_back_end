#!/usr/bin/env python3

"""Hash password"""

import bcrypt

from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Fn hashing password for security purposes"""

    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email=email, hashed_password=hashed_password)

        else:
            raise ValueError(f"User{email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        else:
            database_hashed_password = user.hashed_password

            currentPasswordEntered = password

            is_it_the_same_hash = bcrypt.checkpw(
                currentPasswordEntered.encode("utf-8"),
                database_hashed_password,
            )

            return is_it_the_same_hash
