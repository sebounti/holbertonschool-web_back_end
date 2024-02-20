#!/usr/bin/env python3
""" Module of Index views
"""
from flask import request
from typing import List, TypeVar

class Auth:
    """Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            Define which routes don't need authentication
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Request validation!
        """
        if request is None or ("Authorization" not in request.headers):
            return None

        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """
        nyes
        """
        return None
