#!/usr/bin/env python3
""" AUTHENTICATION CLASS
"""
from base64 import b64decode
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """ authentication class
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ extract base64 auth header
        """
        if authorization_header is None or\
                type(authorization_header) is not str or\
                not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """ decode base64 auth header
        """
        if base64_authorization_header is None or\
                type(base64_authorization_header) is not str:
            return None
        try:
            return b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """ extract user creds
        """
        if decoded_base64_authorization_header is None or\
                type(decoded_base64_authorization_header) is not str or\
                ':' not in decoded_base64_authorization_header:
            return None, None
        creds = decoded_base64_authorization_header.split(':', 1)
        return creds[0], creds[1]

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ returns user from creds
        """
        if user_email is None or type(user_email) is nor str or\
                user_pwd is None or type(user_pwd) is not str:
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        for user in users:
            if User.is_valid_password(user_pwd):
                return user
        return None
