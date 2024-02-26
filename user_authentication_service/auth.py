#!/usr/bin/env python3
"""
encrypting passwords
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Encrypting passwords
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
