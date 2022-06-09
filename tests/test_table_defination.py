from jira_tool.table_defination import *

class TestExcelColumnStore():
    def test_load(self):
        table_defination_filename = 'assets\\table_defination.json'
        store = ExcelColumnStore()
        store.load(table_defination_filename)
        assert store.total_count() > 0

    def test_iter(self):
        table_defination_filename = 'assets\\table_defination.json'
        store = ExcelColumnStore()
        store.load(table_defination_filename)
        items = []
        for item in store:
            items.append(item)
        assert len(items) > 0
