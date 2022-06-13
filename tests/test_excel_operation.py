import pathlib

from jira_tool.excel_defination import *
from jira_tool.excel_operation import *
from jira_tool.sprint_schedule import *

HERE = pathlib.Path(__file__).resolve().parent


class TestExcelOperation:
    def test_read_excel_file(self):
        excel_defination = ExcelDefination()
        excel_defination.load_file(HERE / "files/excel_defination.json")
        sprint_schedule = SprintScheduleStore()
        sprint_schedule.load_file(HERE / "files/sprint_schedule.json")

        columns, stories = read_excel_file(
            HERE / "files/happy_path.xlsx", excel_defination, sprint_schedule
        )
        assert len(columns) == 18
        assert len(stories) == 2
