
from enum import Enum
from typing import Any

__all__ = ["Priority", "convert_to_priority"]

# TODO: Why enum class cannot use classmethod attribute?

class Priority(Enum):
    CRITICAL = 1,
    HIGH = 2,
    MIDDLE = 3,
    LOW = 4,
    NA = 5

    def __str__(self) -> str:
        if self.name == 'NA':
            return 'N/A'
        return self.name.capitalize()

    def __lt__(self, __o: object) -> bool:
        l = -1
        if type(self.value) is tuple:
            l = self.value[0]
        elif type(self.value) is int:
            l = self.value
        r = -1
        if type(__o.value) is tuple:
            r = __o.value[0]
        elif type(__o.value) is int:
            r = __o.value

        if l > r:
            return True
        else:
            return False

    def __eq__(self, __o: object) -> bool:
        if self.value == __o.value:
            return True
        else:
            return False


def convert_to_priority(raw: Any) -> Priority:
    raw = str(raw).strip().upper()
    if raw == 'N/A':
        return Priority.NA
    elif raw == 'LOW':
        return Priority.LOW
    elif raw == 'MEDIUM':
        return Priority.MIDDLE
    elif raw == 'HIGH':
        return Priority.HIGH
    elif raw == 'CRITICAL':
        return Priority.CRITICAL
    return Priority.NA
