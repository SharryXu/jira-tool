'''
Milestone: 2 weeks                                           2022/1/10
Milestone Start Date
Release: 5 weeks (S1 2 weeks S2 2 weeks Harden 1 week)       2022/1/10
S1 Start Date 
S2 Start Date
'''


from typing import Any

from .sprint_schedule import SprintScheduleStore

__all__ = ["Milestone"]


class Milestone(object):
    # TODO: __init__ method cannot have classmethod attribute! Otherwise, all instance will point to the same one.
    def __init__(cls, raw: Any) -> None:
        cls.raw: str = raw
        cls.sprint = cls.raw
        #cls.end_date = convert_to_datetime(cls.raw)
        cls.priority = 0

    def calc_priority(cls, sprintScheduleStore: SprintScheduleStore) -> None:
        if cls.sprint is None:
            cls.priority = 0
        else:
            cls.priority = sprintScheduleStore.get_priority(cls.sprint)

    def __str__(cls) -> str:
        return cls.raw

    def __lt__(cls, __o: object) -> bool:
        if cls.priority < __o.priority:
            return True
        else:
            return False

    def __le__(cls, __o: object) -> bool:
        if cls.priority <= __o.priority:
            return True
        else:
            return False

    def __eq__(cls, __o: object) -> bool:
        if cls.priority == __o.priority:
            return True
        else:
            return False

