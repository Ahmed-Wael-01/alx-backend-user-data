#!/usr/bin/env python3
""" AUTHENTICATION CLASS
"""
from base64 import b64decode
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """ session authentication class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ creates a new session
        """
        if user_id is None or type(user_id) is not str:
            return None
        session_id = uuid4()
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ gets the user id with session id
        """
        if session_id is None or type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)
