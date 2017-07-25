#! /usr/bin/env python

import click
import os

from moss.framework.management.init import init_cli_init_moss_working_directory


@click.command(short_help = 'Initialise a directory with base files')
def init():
<<<<<<< HEAD
    init_cli_init_moss_working_directory()
=======
<<<<<<< HEAD
    init_cli_init_moss_working_directory()
=======
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
>>>>>>> ab66192d9c3f61ae302e0d726ca94d413deaacbf
>>>>>>> 559edc5d7b79e9c511e33ca0f90ff179b5828872
