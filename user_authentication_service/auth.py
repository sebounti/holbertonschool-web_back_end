#!/usr/bin/env python3
"""
encrypting passwords
"""
import bcrypt
from db import DB
from user import User, Base
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """Encrypting passwords
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate a UUID
    """
    return str(uuid4())


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
        '''
        Make session id and update in the database

        Args:
            email: email of the user

        Return:
            session id
        '''
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user((user.id), session_id=session_id)

            return session_id

        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> str:
        '''
        Get user from session id

        Args:
            session_id: session id

        Return:
            user
        '''
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        '''
        Destroy session id

        Args:
            user_id: user id
        '''
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        '''
        Get reset password token

        Args:
            email: email of the user

        Return:
            reset token
        '''
        if email is None:
            raise ValueError("Email cannot be None")

        user = self._db.find_user_by(email=email)

        token: str = _generate_uuid()
        self._db.update_user(user.id, reset_token=token)

        return token
