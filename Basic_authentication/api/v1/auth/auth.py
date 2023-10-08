#!/usr/bin/env python3

"""
Class managing the API authentication.
"""

from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Initialize authentication requirement.

        Args:
            path (str): The path to check for authentication requirement.
            excluded_paths (List[str]): A list of paths that are excluded
                from authentication requirements.

        Returns:
            bool: True if authentication is required for the given path,
                  False if it is excluded.
        """
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True

        slash_tolerant_path = path if path.endswith("/") else path + "/"

        slash_tolerant_excluded_path = [
            path if path.endswith("/") else path + "/"
            for path in excluded_paths
        ]

        if slash_tolerant_path in slash_tolerant_excluded_path:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Initialize authorization requirement.

        Args:
            request: The Flask request object.

        Returns:
            str: The authorization header value.
        """
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """
        Initialize user requirement.

        Args:
            request: The Flask request object.

        Returns:
            TypeVar("User"): The current user.
        """
        return None
