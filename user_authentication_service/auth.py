#!/usr/bin/env python3
"""
encrypting passwords
"""

import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound

def _hash_password(password: str) -> bytes:
    """Encrypting passwords
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def _generate_uuid() -> str:
    """Generate a UUID
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user with the database.

        Args:
            email: user email.
            password: user password.

        Returns:
            User: The user object.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))

        except NoResultFound:
            passwd: str = _hash_password(password)
            user = self._db.add_user(email, passwd)

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate credentials.

        Args:
            email: user email.
            password: user password.

        Returns:
            bool: True if the password is valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ create session user """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None


    def get_user_from_session_id(self, session_id: str) -> str:
        """ Get user from session id """
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """ Generate and reset password token """
        try:
            user = self._db.find_user_by(email=email)
            user.reset_token = _generate_uuid()
            self._db._session.add(user)
            self._db._session.commit()
            return user.reset_token
        except Exception:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """ Method that Updates password """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            if user:
                password = _hash_password(password)
                self._db.update_user(user.id, hashed_password=password,
                                     reset_token=None)
        except NoResultFound:
            raise ValueError

    def destroy_session(self, user_id: int) -> None:
        """ Destroys a session """
        self._db.update_user(user_id, session_id=None)
