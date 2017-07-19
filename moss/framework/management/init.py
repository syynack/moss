#! /usr/bin/env python

import os

from moss.framework.utils import edit_file
from moss.framework.text import ENDPOINTS_BASE_TEXT, TASK_BASE_TEXT

def init_cli_init_moss_working_directory():
    files = ['endpoints', 'task']
    text_mapping = {
        'endpoints': ENDPOINTS_BASE_TEXT,
        'task': TASK_BASE_TEXT
    }

    for filename in files:
        if not os.path.isfile(filename):
            with open(filename, 'w+') as template:
                template.write(text_mapping[filename])

            edit_file(filename)

    if not os.path.exists('.moss'):
        os.makedirs('.moss')
