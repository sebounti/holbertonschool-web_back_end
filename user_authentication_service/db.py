#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
            Add a new user to the database.

        Args:
            email: user email.
            hashed_password: user password.

        Returns:
            User: The user object.

        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """
            Find a user by a given attribute.

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            User: The user object.
        """
        if not kwargs:
            raise InvalidRequestError

        users = self._session.query(User).filter_by(**kwargs).one()

        if users is None:
            raise NoResultFound

        return users

    def update_user(self, user_id: int, **kwargs) -> None:
        """
            Update a user by a given attribute.

        Args:
            user_id: user id.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
        # Récup utilisateur avec l'identifiant user_id de la base de données
        user = self._session.query(User).filter_by(id=user_id).one()

        # Vérifie si  utilisateur n'est trouvé avec l'identifiant spécifié
        if user is None:
            # Si  n'est pas trouvé, lève une exception NoResultFound
            raise NoResultFound

        # Parcourt chaque argument nommé passé à la méthode
        for key, value in kwargs.items():
            # Vérifie si utilisateur a un attribut avec le nom spécifié dans key
            if hasattr(user, key):
                # Si oui, met à jour sa valeur avec celle spécifiée dans value
                setattr(user, key, value)
            else:
                # Si l'attribut n'existe pas, lève une exception ValueError
                raise ValueError

        # envoye changements à la base de données
        self._session.commit()
