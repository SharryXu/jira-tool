import datetime
import re
from decimal import *
from typing import Any

from dateutil import parser

__all__ = ["Story", "convert_to_bool",
           "convert_to_datetime", "convert_to_decimal"]


def convert_to_bool(raw: Any) -> bool:
    raw = str(raw).strip().upper()
    if raw == 'YES':
        return True
    else:
        return False


def convert_to_decimal(raw: Any) -> Decimal:
    raw = str(raw).strip()
    pattern = re.compile('[0-9.]{1,10}')
    result = pattern.search(raw)
    if result is not None:
        return Decimal(result.group())
    else:
        return Decimal(0)


def convert_to_datetime(raw: Any) -> datetime:
    raw = str(raw).strip()
    pattern = re.compile('[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{2,4}')
    result = pattern.search(raw)
    if result is not None:
        return parser.parse(result.group())
    else:
        return None


class Story(object):
    @classmethod
    def __init__(cls) -> None:
        pass
