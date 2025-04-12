#!/usr/bin/env python3
""" authentication module
"""
import bcrypt
from user import User
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> str:
    """ hashes a password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ generates a random uuid
    """
    return str(uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """ validate login procedure
        """
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode(), user.hashed_password):
                return True
            return False
        except Exception as e:
            return False

    def create_session(self, email: str) -> str:
        """ creates a new user session
        """
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            return None
        new_id = _generate_uuid()
        user.session_id = new_id
        return new_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """ gets user from session
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ destroy user session
        """
        try:
            user = self._db.find_user_by(id=user_id)
            user.session_id = None
        finally:
            return None
