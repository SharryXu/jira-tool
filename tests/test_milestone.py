
import pathlib

from src.jira_tool.milestone import Milestone
from src.jira_tool.sprint_schedule import *

HERE = pathlib.Path(__file__).resolve().parent

class TestMilestone():
    def test_init(self):
        schedule_filename = HERE.parent / 'src/jira_tool/assets/sprint_schedule.json'
        store = SprintScheduleStore()
        store.load_file(schedule_filename)
 
        milestone = Milestone('R134 S1')
        milestone.calc_priority(store)
        assert milestone.priority == 1
