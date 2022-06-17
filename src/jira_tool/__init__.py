# -*- coding: utf-8 -*-
import logging.config
from importlib import metadata
from importlib.resources import files

from .excel_defination import ExcelDefination
from .excel_operation import (
    output_to_csv_file,
    output_to_excel_file,
    process_excel_file,
    read_excel_file,
)
from .milestone import Milestone
from .priority import Priority
from .sprint_schedule import SprintScheduleStore
from .story import (
    Story,
    sort_stories,
    sort_stories_by_deferred,
    sort_stories_by_override,
)

__version__ = metadata.version("sharry_jira_tool")

__all__ = [
    "ExcelDefination",
    "read_excel_file",
    "output_to_csv_file",
    "output_to_excel_file",
    "process_excel_file",
    "Milestone",
    "Priority",
    "SprintScheduleStore",
    "Story",
    "sort_stories",
    "sort_stories_by_deferred",
    "sort_stories_by_override",
]

del metadata


logging.config.fileConfig(str(files("jira_tool.assets").joinpath("logging.conf")))
