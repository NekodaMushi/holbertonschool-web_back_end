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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Check if password is valid

    Args:
        password (str): The password to hash.
        hashed_password (bytes): The hashed password as bytes.

    Returns:
        boolean: True of False
    """
    if bcrypt.checkpw(password.encode("utf-8"), hashed_password):
        return True
    return False
