import pathlib

from src.jira_tool.excel_defination import *

HERE = pathlib.Path(__file__).resolve().parent

class TestExcelDefination():
    def test_load(self):
        table_defination_filename = HERE.parent / 'src/jira_tool/assets/excel_defination.json'
        store = ExcelDefination()
        store.load_file(table_defination_filename)
        assert store.total_count() > 0

    def test_iter(self):
        table_defination_filename = HERE.parent / 'src/jira_tool/assets/excel_defination.json'
        store = ExcelDefination()
        store.load_file(table_defination_filename)
        items = []
        for item in store:
            items.append(item)
        assert len(items) > 0
