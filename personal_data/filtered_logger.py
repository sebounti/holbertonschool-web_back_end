#!/usr/bin/env python3
''' Filtered logger '''
import re
from typing import List
import logging
import mysql.connector
import os

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


'''Task 0 - Regex-ing'''


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    ''' Returns the log message obfuscated '''
    for field in fields:
        message = re.sub(f'{field}=.+?{separator}',
                         f'{field}={redaction}{separator}', message)

    return message


'''Task 1 - Log formatter '''


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        ''' Format the record '''
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)

        return (super(RedactingFormatter, self).format(record))


'''Task 2 - Create logger '''


def get_logger() -> logging.Logger:
    ''' Returns a logging object '''
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream = logging.StreamHandler()
    stream.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    logger.addHandler(stream)

    return logger


''' Task 3 - Connect to secure database '''


def get_db() -> mysql.connector.connection.MySQLConnection:
    ''' Returns a connector to a database '''

    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    hosting = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    database = mysql.connector.connect(
        host=hosting,
        user=username,
        password=password,
        database=db_name
    )

    return database
