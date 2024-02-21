#!/usr/bin/env python3

""" Basic authentication module"""

from api.v1.auth.auth import Auth
from typing import List, TypeVar
from flask import request


class BasicAuth(Auth):
    '''
        Basic authentication class'
    '''
    def extract_base64_authorization_header(self, authorization_header:
                                            str) -> str:

        """ Extract Base 64 Authorization Header """

        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        encoded = authorization_header.split(' ', 1)[1]

        return encoded
