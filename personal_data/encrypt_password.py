#!/usr/bin/env python3

import bcrypt

''' Task 5 - Encrypting passwords'''


def hash_password(password: str = '') -> bytes:
    ''' Returns a hashed password '''
    return bcrypt.hashpw(password.encode('utf-8'),
                         bcrypt.gensalt(prefix=b"2b"))
