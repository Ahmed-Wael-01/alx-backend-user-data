#!/usr/bin/env python3
""" AUTHENTICATION CLASS
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


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
