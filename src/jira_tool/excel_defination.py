import json
from datetime import datetime

from .milestone import Milestone
from .priority import Priority

__all__ = ["ExcelDefination"]


class ExcelDefination:
    def __init__(self) -> None:
        self.store: list[tuple] = []

    def load(self, content: str):
        if content is None:
            return
        raw_data = json.loads(content)

        for item in raw_data:
            column_index = 0
            column_name = None
            column_type = None
            column_sorted = False
            column_isDesc = False

            for key, value in item.items():
                if key.lower() in "index":
                    column_index = value
                if key.lower() in "name":
                    column_name = value
                if key.lower() in "type":
                    column_type = ExcelDefination.convert_str_to_type(value)
                if key.lower() in "sorted":
                    column_sorted = value
                if key.lower() in "isdesc":
                    column_isDesc = value

            self.store.append(
                (column_index, column_name, column_type, column_sorted, column_isDesc)
            )

    def load_file(self, file_path: str):
        if file_path is None:
            return
        with open(file=file_path, mode="r") as table_defination_file:
            raw_data = json.load(table_defination_file)

            for item in raw_data:
                column_index = 0
                column_name = None
                column_type = None
                column_sorted = False
                column_isDesc = False

                for key, value in item.items():
                    if key.lower() in "index":
                        column_index = value
                    if key.lower() in "name":
                        column_name = value
                    if key.lower() in "type":
                        column_type = ExcelDefination.convert_str_to_type(value)
                    if key.lower() in "sorted":
                        column_sorted = value
                    if key.lower() in "isdesc":
                        column_isDesc = value

                self.store.append(
                    (
                        column_index,
                        column_name,
                        column_type,
                        column_sorted,
                        column_isDesc,
                    )
                )

    @staticmethod
    def convert_str_to_type(type_str: str) -> type:
        type_str = str(type_str).strip().lower()
        if type_str == "str":
            return str
        elif type_str == "bool":
            return bool
        elif type_str == "datetime":
            return datetime
        elif type_str == "priority":
            return Priority
        elif type_str == "milestone":
            return Milestone
        else:
            return None

    def __iter__(self):
        for item in self.store:
            yield item

    def get_columns(self) -> list[tuple]:
        result = []
        for item in self.store:
            result.append(item)
        return result

    def total_count(self):
        return len(self.store)
