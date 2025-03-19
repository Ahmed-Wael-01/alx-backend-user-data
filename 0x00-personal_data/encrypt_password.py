#!/usr/bin/env python3
"""
encryption ya broooo
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ hashing passwords """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt(12))


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ validate password """
    if bcrypt.checkpw(password.encode(), hashed_password):
        return True
    return False
