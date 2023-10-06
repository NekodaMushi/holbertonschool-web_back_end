#!/usr/bin/env python3

"""
Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The hashed password as bytes.
    """
    salt = bcrypt.gensalt(rounds=14)
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password
