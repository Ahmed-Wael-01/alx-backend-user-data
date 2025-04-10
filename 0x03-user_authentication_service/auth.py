#!/usr/bin/env python3
""" authentication module
"""
import bcrypt
from user import User
from db import DB
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """ hashes a password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ register a new user
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashedpw = _hash_password(password)
            user = self._db.add_user(email, hashedpw)
            return user
        raise ValueError("User {} already exists".format(email))
