Jira Tool - userful tool to sort jira stories
=============================================

|pypi| |python 3.7| |python 3.10|

.. |PyPI| image:: https://img.shields.io/pypi/v/sharry-jira-tool.svg?style=flat-square
    :target https://pypi.org/project/sharry-jira-tool/
    :alt: pypi version

.. |python 3.7| image:: https://github.com/SharryXu/jira-tool/actions/workflows/python-3-7-test.yml/badge.svg
    :target: https://github.com/SharryXu/jira-tool/actions/workflows/python-3-7-test.yml
    :alt: python 3.7

.. |python 3.10| image:: https://github.com/SharryXu/jira-tool/actions/workflows/python-3-10-test.yml/badge.svg
    :target: https://github.com/SharryXu/jira-tool/actions/workflows/python-3-10-test.yml
    :alt: python 3.10

Installation
============
`jira-tool` can be installed from PyPI using `pip` (note that the package name is different from the importable name)::

    pip install -U sharry-jira-tool

Download
========
jira-tool is available on PyPI
https://pypi.org/project/sharry-jira-tool

Code
====
The code and issue tracker are hosted on GitHub:
https://github.com/SharryXu/jira-tool

Features
========

* Parsing the excel file which usually been downloaded from the Jira platform.
* Sorting the excel records using some specific logic.
* Generating the target excel file which contains the result.

Quick example
=============
Here's a simple program, just to give you an idea about how to use this package.

>>> import pathlib
>>> from jira_tool import process_excel_file
>>> HERE = pathlib.Path().resolve()
>>> process_excel_file(HERE / "source.xlsx", HERE / "target.xlsx")

Author
======
The jira-tool module was written by Sharry Xu <sharry.xu@outlook.com> in 2022.
The original idea comes from Andy Wu <andy.wu@greendotcorp.com>.

Starting with version 0.1.13, the main function of this project has been totally finished.

Contact
=======
Our mailing list is available at `sharry.xu@outlook.com`.

License
=======
All contributions after December 1, 2022 released under MIT license.
