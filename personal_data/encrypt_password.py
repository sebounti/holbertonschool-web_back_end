#!/usr/bin/env python3
''' Task 5 - Encrypting passwords'''

import bcrypt

'''task 5 - Encrypting passwords'''


def hash_password(password: str = '') -> bytes:
    ''' Returns a hashed password '''
    return bcrypt.hashpw(password.encode('utf-8'),
                         bcrypt.gensalt(prefix=b"2b"))


''' Task 6 - Check valid password '''


def is_valid(hashed_password: bytes, password: str) -> bool:
    ''' Returns a hashed password '''
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
