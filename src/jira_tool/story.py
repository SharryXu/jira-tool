import re
from datetime import datetime
from decimal import *
from operator import attrgetter
from typing import Any

from attr import attributes
from dateutil import parser

from .milestone import *
from .priority import *

__all__ = [
    "Story",
    "convert_to_bool",
    "convert_to_datetime",
    "convert_to_decimal",
    "sort_stories",
    "sort_stories_by_deferred",
    "sort_stories_by_override",
]


def convert_to_bool(raw: Any) -> bool:
    raw = str(raw).strip().upper()
    if raw == "YES":
        return True
    else:
        return False


def convert_to_decimal(raw: Any) -> Decimal:
    raw = str(raw).strip()
    pattern = re.compile("[0-9.]{1,10}")
    result = pattern.search(raw)
    if result is not None:
        return Decimal(result.group())
    else:
        return Decimal(0)


def convert_to_datetime(raw: Any) -> (datetime | None):
    if raw is None:
        return
    raw = str(raw).strip()
    return parser.parse(raw)


class Story(object):
    def __init__(self, columns: list[tuple] = None) -> None:
        if columns is None:
            return
        self.attributes = columns
        for column in columns:
            if column[2] is str:
                setattr(self, column[1], "")
            elif column[2] is bool:
                setattr(self, column[1], False)
            elif column[2] is Priority:
                setattr(self, column[1], Priority.NA)
            elif column[2] is Milestone:
                setattr(self, column[1], None)
            elif column[2] is datetime:
                setattr(self, column[1], None)

    def get_value(self, property_name: str) -> str:
        property = getattr(self, property_name, None)
        if property is None:
            return ""
        elif type(property) is datetime:
            return property.date().isoformat()
        else:
            return str(property)

    def __str__(self):
        if self.attributes is None:
            return ""
        else:
            result = ""
            for attribute in self.attributes:
                result += str(getattr(self, attribute))
            return result


def sort_stories(stories: list[Story], excel_defination_columns: list[tuple]):
    sort_rule = []

    for _, column_name, _, need_sort, sort_desc_or_asc in excel_defination_columns:
        if need_sort is True:
            sort_rule.append((column_name, sort_desc_or_asc))

    _internal_sort_stories(stories, sort_rule)


def _internal_sort_stories(stories: list[Story], keys: list[tuple]):
    for key, isReversed in reversed(keys):
        stories.sort(key=attrgetter(key), reverse=isReversed)


def sort_stories_by_deferred(stories: list[Story]) -> list[Story]:
    return _raise_story_priority(stories, "deferred")


def sort_stories_by_override(stories: list[Story]) -> list[Story]:
    return _raise_story_priority(stories, "override")


"""
Only bool indicator for now
"""


def _raise_story_priority(stories: list[Story], attribute_name: str) -> list[Story]:
    if stories is None or len(stories) == 0:
        return
    if not hasattr(stories[0], attribute_name):
        return
    result = [None] * len(stories)
    j = 0
    for i in range(len(stories)):
        if getattr(stories[i], attribute_name) is True:
            result[j] = stories[i]
            j += 1
    for i in range(len(stories)):
        if getattr(stories[i], attribute_name) is False:
            result[j] = stories[i]
            j += 1
    return result
