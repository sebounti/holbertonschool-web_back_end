#!/usr/bin/env python3
""" Basic authentication module"""

from api.v1.auth.auth import Auth
from typing import List, TypeVar
from base64 import b64decode
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

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:

        """ Decodes the value of a base64 string """

        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            encoded = base64_authorization_header.encode('utf-8')
            decoded64 = b64decode(encoded)
            decoded = decoded64.decode('utf-8')
        except BaseException:
            return None

        return decoded

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):

        '''
        Extracts user credentials from the decoded base64 string.
        Returns a tuple of the user email and password, in that order.
        '''

        if decoded_base64_authorization_header is None:
            return (None, None)

        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)

        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        user_credentials = decoded_base64_authorization_header.split(':', 1)

        return (user_credentials[0], user_credentials[1])
