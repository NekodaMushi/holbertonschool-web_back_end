#!/usr/bin/env python3

"""Hash password"""

import bcrypt

from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """Fn hashing password for security purposes"""

    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Fn representing a new UUID"""
    return str(uuid.uuid1())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Record new User"""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email=email,
                                     hashed_password=hashed_password)

        else:
            raise ValueError(f"User{email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """Check if login/password are correct"""
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

    def get_user_from_session_id(self, session_id: str) -> User:
        """Find user using the session id"""
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        else:
            return user

    def create_session(self, email: str) -> str:
        """Create new session - Login"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        else:
            user.session_id = _generate_uuid()
            return user.session_id

    def destroy_session(self, user_id: int) -> None:
        """Close session - Logout"""
        try:
            user = self._db.find_user_by(id=user_id)
        except NoResultFound:
            return None
        else:
            self._db.update_user(user.id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """Allow user to reset his password"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        else:
            user.reset_token = _generate_uuid()
            return user.reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """Changes user's password"""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError
        else:
            hashed_password = _hash_password(password)
        self._db.update_user(user.id, hashed_password=hashed_password,
                             reset_token=None)
