#!/usr/bin/env python3
""" authentication module
"""
import bcrypt


def __hash__password(password: str) -> str:
    """ hashes a password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
