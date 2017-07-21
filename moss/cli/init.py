#! /usr/bin/env python

import click
import os

from moss.utils import edit_file
from moss.text import ENDPOINTS_BASE_TEXT, TASK_BASE_TEXT


@click.command(short_help = 'Initialise a directory with base files')
def init():
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
