#!/usr/bin/env python3
"""
Module of Index views
"""

from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    '''
        Session Authentication
    '''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:

        ''' Create a session'''
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        self.user_id_by_session_id[session_id] = user_id
        return session_id
