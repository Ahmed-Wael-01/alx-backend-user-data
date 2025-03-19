#!/usr/bin/env python3
"""
filter datum
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    logging messages
    """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
