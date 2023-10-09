#!/usr/bin/python3

"""Hash password"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """Fn hashing password for security purposes"""

    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
