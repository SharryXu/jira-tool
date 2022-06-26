import math
import re
from datetime import datetime
from decimal import *
from operator import attrgetter
from typing import Any

from dateutil import parser

from .excel_defination import ExcelDefination
from .milestone import *
from .priority import *
from .sprint_schedule import SprintScheduleStore

__all__ = [
    "Story",
    "StoryFactory",
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
    def __init__(self, columns: list[tuple], compare_rules: list[tuple]) -> None:
        if columns is None:
            raise ValueError("Columns must be provided!")
        self.compare_rules = compare_rules
        self.columns = columns
        for column in self.columns:
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
            else:
                setattr(self, column[1], None)

    def get_value(self, property_name: str) -> str:
        property = getattr(self, property_name, None)
        if property is None:
            return ""
        elif type(property) is datetime:
            return property.date().isoformat()
        else:
            return str(property)

    def __getitem__(self, property_name):
        return self.get_value(property_name)

    def set_value(self, property_type: Any, property_name: str, property_value: Any):
        if property_type is str:
            setattr(self, property_name, property_value)
        elif property_type is bool:
            setattr(self, property_name, convert_to_bool(property_value))
        elif property_type is Priority:
            setattr(self, property_name, convert_to_priority(property_value))
        elif property_type is datetime:
            setattr(self, property_name, convert_to_datetime(property_value))
        elif property_type is Milestone:
            milestone = Milestone(property_value)
            setattr(self, property_name, milestone)
        else:
            setattr(self, property_name, property_value)

    def __setitem__(self, property_name, property_value):
        if type(property_value) is str:
            self.set_value(str, property_name, property_value)
        elif type(property_value) is str:
            self.set_value(str, property_name, property_value)
        elif type(property_value) is str:
            self.set_value(str, property_name, property_value)
        elif type(property_value) is str:
            self.set_value(str, property_name, property_value)
        elif type(property_value) is str:
            self.set_value(str, property_name, property_value)
        else:
            self.set_value(type(property_value), property_name, property_value)

    def __lt__(self, __o: object) -> bool:
        return compare_story(self, __o) < 0

    def __le__(self, __o: object) -> bool:
        return compare_story(self, __o) <= 0

    def __gt__(self, __o: object) -> bool:
        return compare_story(self, __o) > 0

    def __ge__(self, __o: object) -> bool:
        return compare_story(self, __o) >= 0

    def __eq__(self, __o: object) -> bool:
        return compare_story(self, __o) == 0

    def __str__(self):
        separator = ", "
        if self.columns is None:
            return ""
        else:
            result = ""
            for _, column_name, _, _, _, _ in self.columns:
                if hasattr(self, column_name):
                    result += f"{str(getattr(self, column_name))}{separator}"
            return result


class StoryFactory(object):
    def __init__(self, columns: list[tuple]) -> None:
        if columns is None:
            raise ValueError("Columns must be provided!")
        self.columns = columns
        self.compare_rules = self.__generate_compare_rules()

    def __generate_compare_rules(self) -> list[tuple]:
        compare_rules = []
        for _, column_name, _, _, _, priority in self.columns:
            if priority > 0:
                compare_rules.append((column_name, priority))
        compare_rules.sort(key=lambda r: r[1], reverse=True)
        return compare_rules

    def create_story(self) -> Story:
        return Story(self.columns, self.compare_rules)


def compare_story(a: Story, b: Story) -> int:
    """
    Compare two stories.

    :parm a:
        First story
    :parm b:
        Second story
    :parm sort_rule:
        Priority information
    :return
        1: means a > b
        0: means a == b
        -1: means a < b
    """
    if (
        a.compare_rules is None
        or b.compare_rules is None
        or a.compare_rules != b.compare_rules
    ):
        raise ValueError("The compare rules is invalid.")

    for name, _ in a.compare_rules:
        if a[name] > b[name]:
            return 1
        elif a[name] < b[name]:
            return -1
        else:
            continue
    return 0


def sort_stories(stories: list[Story], excel_defination: ExcelDefination):
    sort_rule = []
    excel_defination_columns = excel_defination.get_columns()

    for _, column_name, _, need_sort, sort_desc_or_asc, _ in excel_defination_columns:
        if need_sort is True:
            sort_rule.append((column_name, sort_desc_or_asc))

    _internal_sort_stories(stories, sort_rule)


def _internal_sort_stories(stories: list[Story], keys: list[tuple]):
    for key, isReversed in reversed(keys):
        stories.sort(key=attrgetter(key), reverse=isReversed)


"""
def sort_stories_by_priority(
    stories: list[Story], excel_defination: ExcelDefination
) -> list[Story]:
    sort_rule = []
    excel_defination_columns = excel_defination.get_columns()

    for _, column_name, _, _, _, priority in excel_defination_columns:
        if priority > 0:
            sort_rule.append((column_name, priority))
    sort_rule.sort(key=lambda r: r[1], reverse=True)

    result = []
    while len(stories) > 0:
        tmp = []
        for priority in Priority:
            for name, sort_priority in sort_rule:
                for story in stories:
                    # if story[name]
                    continue

    return result
"""


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
