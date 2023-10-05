#!/usr/bin/env python3

"""
    Filtering for privacy - Filter datum
"""

from typing import List
import re
import logging

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR
        )

        return super().format(record)


# def get_logger() -> logging.Logger:


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """
    Filter sensitive information in a message.

    Args:
        fields (List[str]): A list of strings representing
        all fields to obfuscate
        redaction (str): Ta string representing by what
        the field will be obfuscated
        message (str): a string representing the log line.
        separator (str): a string representing by which character
        is separating all fields in the log line

    Returns:
        str: log message obfuscated.

    """
    for field in fields:
        message = re.sub(
            field + "=.+?" + separator, field + "=" + redaction + separator, message
        )
    return message
