#!/usr/bin/env python3
""" AUTHENTICATION CLASS
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require authentication
        """
        if path is None or excluded_paths is None:
            return True
        for item in excluded_paths:
            if path is item or item == path + '/':
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ auth header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user
        """
        return None
