#!/usr/bin/env python3
"""
encryption ya broooo
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ hashing passwords """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt(12))
