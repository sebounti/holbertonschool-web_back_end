#!/usr/bin/env python3
''' Filtered logger '''
import re


def filter_datum(fields, redaction, message, separator):
    ''' Returns the log message obfuscated '''
    return re.sub(r'({})(?={}|$)'.format('|'.join(fields), separator),
                  redaction, message)
