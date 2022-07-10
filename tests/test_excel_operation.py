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
        assert len(stories) == 5

    def test_process_excel_file(self):
        process_excel_file(
            HERE / "files/happy_path.xlsx",
            HERE / "files/happy_path_sorted.xlsx",
            sprint_schedule_config=str(HERE / "files/sprint_schedule.json"),
            excel_defination_config=str(HERE / "files/excel_defination.json"),
        )

        excel_defination = ExcelDefination()
        excel_defination.load_file(HERE / "files/excel_defination.json")
        sprint_schedule = SprintScheduleStore()
        sprint_schedule.load_file(HERE / "files/sprint_schedule.json")

        _, stories = read_excel_file(
            HERE / "files/happy_path.xlsx", excel_defination, sprint_schedule
        )

        for i in range(len(stories) - 1):
            if (
                stories[i]["milestone"] == stories[i + 1]["milestone"]
                and stories[i]["criticalDefect"] == stories[i + 1]["criticalDefect"]
            ):
                assert stories[i] <= stories[i + 1]
