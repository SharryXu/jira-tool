from jira_tool.sprint_schedule import *


class TestSprintSchedule():
    def test_load_sprint_schedule(self):
        schedule_filename = 'assets\\sprint_schedule.json'
        store = SprintScheduleStore()
        store.load(schedule_filename)
        assert store.total_count() > 0

    def test_get_priority(self):
        schedule_filename = 'assets\\sprint_schedule.json'
        store = SprintScheduleStore()
        assert store.get_priority('R134 S2') == 0

        store.load(schedule_filename)
        assert store.get_priority('R134 S2') == 2
 

