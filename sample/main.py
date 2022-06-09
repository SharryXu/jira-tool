import pathlib

from jira_tool.excel_operation import (output_to_excel_file, read_excel_file,
                                         sort_stories)
from jira_tool.sprint_schedule import *
from jira_tool.table_defination import *

# Current directory
HERE = pathlib.Path(__file__).resolve().parent

if __name__ == '__main__':
    path = HERE.parent / 'docs/red.xlsx'

    sprint_schedule = SprintScheduleStore()
    sprint_schedule.load(HERE.parent / 'assets/sprint_schedule.json')

    table_defination = ExcelColumnStore()
    table_defination.load(HERE.parent / 'assets/table_defination.json')
    excel_columns = table_defination.to_list()

    columns, stories = read_excel_file(path, excel_columns, sprint_schedule)

    sort_stories(stories, excel_columns)
    #sort_stories_by_deferred(stories)
    #sort_stories_by_override(stories)

    output_to_excel_file('sorted.xlsx', columns, stories, excel_columns)
