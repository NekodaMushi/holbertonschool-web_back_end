#!/usr/bin/env python3

"""
Class managing the API authentication.
"""

from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Init auth requirement"""
        return False

    def authorization_header(self, request=None) -> str:
        """Init authorization requirement"""
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """Init user requirement"""
        return None
