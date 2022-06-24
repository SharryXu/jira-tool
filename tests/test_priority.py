from jira_tool.priority import *
from jira_tool.story import *


class TestPriority:
    def test_compare_priority(self):
        p1: Priority = Priority.CRITICAL
        p2: Priority = Priority.HIGH
        p3: Priority = Priority.HIGH
        p4: Priority = Priority.MIDDLE
        p5: Priority = Priority.LOW
        p6: Priority = Priority.NA

        assert p1 > p2
        assert p2 < p1
        assert p2 == p3
        assert p3 > p4
        assert p4 < p3
        assert p4 > p5
        assert p5 < p4
        assert p5 > p6
        assert p6 < p5

    def test_priority_to_str(self):
        p1: Priority = Priority.CRITICAL
        p2: Priority = Priority.NA
        assert str(p1) == "Critical"
        assert str(p2) == "N/A"
