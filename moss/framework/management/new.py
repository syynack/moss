#! /usr/bin/env python

import sys
import os

from moss.framework.utils import edit_file
from moss.framework.text import TASK_BASE_TEXT, ENDPOINTS_BASE_TEXT

def _create_file(name, contents):
    if not os.path.isfile(name):
        with open(name, 'w+') as template:
            template.write(contents)


def _edit_file(name, contents):
    if not os.path.isfile(name):
        with open(name, 'w+') as template:
            template.write(contents)
            edit_file(template)
            sys.exit(0)

    print '{} already exists.'.format(name)


def new_cli_create_endpoints_file(edit, output):
    if edit:
        _edit_file(output, ENDPOINTS_BASE_TEXT)

    _create_file(output, ENDPOINTS_BASE_TEXT)


def new_cli_create_module_file(edit, output):
    if edit:
        _edit_file(output, MODULE_BASE_TEXT)

    _create_file(output, MODULE_BASE_TEXT)


def new_cli_create_task_file(edit, output):
    if edit:
        _edit_file(output, TASK_BASE_TEXT)

    _create_file(output, TASK_BASE_TEXT)
