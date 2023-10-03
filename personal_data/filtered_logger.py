#!/usr/bin/env python3

"""
    Filtering for privacy - Filter datum
"""

from typing import List
import re


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
            field + "=.+?" + separator,
            field + "=" + redaction + separator, message
        )
    return message
