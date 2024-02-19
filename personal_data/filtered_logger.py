#!/usr/bin/env python3
''' Filtered logger '''
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: list):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        ''' Format the record '''
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)

        return (super(RedactingFormatter, self).format(record))


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    ''' Returns the log message obfuscated '''
    for field in fields:
        message = re.sub(f'{field}=.+?{separator}',
                         f'{field}={redaction}{separator}', message)

    return message
