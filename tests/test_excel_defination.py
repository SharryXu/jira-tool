import pathlib

import pytest

from jira_tool.excel_defination import *

HERE = pathlib.Path(__file__).resolve().parent


class TestExcelDefination:
    def test_load_happy_path(self):
        excel_defination_filename = HERE / "files/excel_defination.json"

        store = ExcelDefination()
        with open(excel_defination_filename) as file:
            store.load(file.read())
        assert store.total_count() > 0

    def test_load_using_none_input(self):
        store = ExcelDefination()
        with pytest.raises(ValueError) as err:
            store.load(None)
        assert "invalid" in str(err.value)

    def test_load_file(self):
        excel_defination_filename = HERE / "files/excel_defination.json"
        store = ExcelDefination()
        store.load_file(excel_defination_filename)
        assert store.total_count() > 0

    def test_load_file_none(self):
        store = ExcelDefination()
        with pytest.raises(ValueError) as err:
            store.load_file(None)
        assert "invalid" in str(err.value)

    def test_iter(self):
        excel_defination_filename = HERE / "files/excel_defination.json"
        store = ExcelDefination()
        store.load_file(excel_defination_filename)
        items = []
        for item in store:
            items.append(item)
        assert len(items) > 0
