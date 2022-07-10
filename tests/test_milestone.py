import pathlib

from jira_tool.milestone import Milestone
from jira_tool.sprint_schedule import *

HERE = pathlib.Path(__file__).resolve().parent


class TestMilestone:
    def test_init(self):
        schedule_filename = HERE.parent / "src/jira_tool/assets/sprint_schedule.json"
        store = SprintScheduleStore()
        store.load_file(schedule_filename)

        milestone = Milestone("R134 S1")
        milestone.calc_priority(store)
        assert milestone.priority == 1

    def test_compare(self):
        schedule_filename = HERE.parent / "src/jira_tool/assets/sprint_schedule.json"
        store = SprintScheduleStore()
        store.load_file(schedule_filename)

        m1 = Milestone("M109")
        m1.calc_priority(store)
        m2 = Milestone("M110")
        m2.calc_priority(store)
        m3 = Milestone("m110")
        m3.calc_priority(store)
        m4 = Milestone("R134 S2")
        m4.calc_priority(store)
        m5 = Milestone("R134 s2")
        m5.calc_priority(store)
        assert m1 < m2
        assert m2 == m3
        assert m3 == m4
        assert m4 == m5
