import logging
from importlib import metadata

from . import *

__version__ = metadata.version('sharry_jira_tool')

__all__ = ["excel_defination", "excel_operation",
           "milestone", "priority", "sprint_schedule", "story"]

del metadata

logging.basicConfig(filename='jira_tool.log',
                    format='%(asctime)s : %(levelname)s:%(message)s')
