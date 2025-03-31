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
            l_item = len(item)
            if l_item is 0:
                continue
            if path == item or item == path + '/':
                return False
            if item[-1] == '*':
                if item[:-1] == path[:l_item - 1]:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """ auth header
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user
        """
        return None
