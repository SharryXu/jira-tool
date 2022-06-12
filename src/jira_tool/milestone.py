"""
Milestone: 2 weeks                                           2022/1/10
Milestone Start Date
Release: 5 weeks (S1 2 weeks S2 2 weeks Harden 1 week)       2022/1/10
S1 Start Date 
S2 Start Date
"""


from typing import Any

from .sprint_schedule import SprintScheduleStore

__all__ = ["Milestone"]


class Milestone(object):
    # TODO: __init__ method cannot have classmethod attribute! Otherwise, all instance will point to the same one.
    def __init__(self, raw: Any) -> None:
        self.raw: str = raw
        self.sprint = self.raw
        self.priority = 0

    def calc_priority(self, sprint_schedule: SprintScheduleStore) -> None:
        if self.sprint is None:
            self.priority = 0
        else:
            self.priority = sprint_schedule.get_priority(self.sprint)

    def __str__(self) -> str:
        return self.raw

    def __lt__(self, __o: object) -> bool:
        if self.priority < __o.priority:
            return True
        else:
            return False

    def __le__(self, __o: object) -> bool:
        if self.priority <= __o.priority:
            return True
        else:
            return False

    def __eq__(self, __o: object) -> bool:
        if self.priority == __o.priority:
            return True
        else:
            return False

    def __str__(self):
        return self.raw
