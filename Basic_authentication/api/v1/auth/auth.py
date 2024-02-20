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
        '''
            Define which routes don't need authentication
        '''
        if path is None:
            return True
        if not excluded_paths or excluded_paths == []:
            return True
        for excluded_path in excluded_paths:
            if excluded_path.endswith("/"):
                if path.startswith(excluded_path):
                    return False
            elif path == excluded_path:
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
