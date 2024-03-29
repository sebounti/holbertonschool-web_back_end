#!/usr/bin/env python3
"""
encrypting passwords
"""

import bcrypt
import uuid
from db import DB
from user import User
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
            # If no user is found, proceed with adding the user
            hashed_password: str = _hash_password(password)
            # Add the new user to the database
            user = self._db.add_user(email, hashed_password)
            return user

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
        """
        create session user
        """
        try:
            # retrieve user
            user = self._db.find_user_by(email=email)
            # generate a new session id
            session_id = _generate_uuid()
            # update user session id
            self._db.update_user(user.id, session_id=session_id)
            # return session id
            return session_id
        except NoResultFound:
            # if user does not exist
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

    def destroy_session(self, user_id: int) -> None:
        """ Destroys a session """
        try:
            self._db.update_user(user_id, session_id=None)
            return None

        except Exception:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """ Generate and reset password token """
        if email is None:
            return None

        try:
            user = self._db.find_user_by(email=email)
            token: str = _generate_uuid()
            self._db.update_user(user.id, reset_token=token)
            return token

        except (NoResultFound, InvalidRequestError):
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """ Method that Updates password """
        if reset_token is None or password is None:
            return None

        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except (NoResultFound, InvalidRequestError) as e:
            raise ValueError

        n_passwd: str = _hash_password(password)
        self._db.update_user(user.id, hashed_password=n_passwd,
                             reset_token=None)

        return None
