import logging
from importlib import metadata

from .excel_defination import *
from .excel_operation import *
from .milestone import *
from .priority import *
from .sprint_schedule import *
from .story import *

__version__ = metadata.version('sharry_jira_tool')

del metadata

logging.basicConfig(filename='jira_tool.log',
                    format='%(asctime)s : %(levelname)s:%(message)s')
