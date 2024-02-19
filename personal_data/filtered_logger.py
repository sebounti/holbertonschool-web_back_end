#!/usr/bin/env python3
''' Filtered logger '''
from re import sub
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    ''' Returns the log message obfuscated '''
    for field in fields:
        message = sub(f'{field}=.+?{separator}',
                      f'{field}={redaction}{separator}', message)

    return message
