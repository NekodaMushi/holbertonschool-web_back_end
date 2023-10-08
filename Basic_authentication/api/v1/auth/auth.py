#!/usr/bin/env python3

"""
Class managing the API authentication.
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Class authentification"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Init auth requirement"""
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == "":
            return True

        slash_tolerant_path = path if path.endswith("/") else path + "/"

        slash_tolerant_excluded_path = [
            path if path.endswith("/") else path + "/" for path in excluded_paths
        ]

        if slash_tolerant_path in slash_tolerant_excluded_path:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Init authorization requirement"""
        if request is None:
            return None
        if "Authorization" not in request.header:
            return None
        return request.header["Authorization"]

    def current_user(self, request=None) -> TypeVar("User"):
        """Init user requirement"""
        return None
