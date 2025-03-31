#!/usr/bin/env python3
""" AUTHENTICATION CLASS
"""
from base64 import b64decode
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class sessionAuth(Auth):
    """ session authentication class
    """
    pass
