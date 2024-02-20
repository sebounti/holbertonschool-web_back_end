#!/usr/bin/env python3
""" Module of Index views
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            Define which routes don't need authentication
        """
        if path is None or ex_path is None or len(ex_path) == 0:
            return True
        for ex_path in excluded_paths:
            if ex_path == path:
                return False
            if ex_path.endswith('*'):
                pfx_path = ex_path[:-1]
            if pfx_path in path:
                return False

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
