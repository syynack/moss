#! /usr/bin/env python

import click
import utils

from text import ENDPOINTS_BASE_TEXT, TASK_BASE_TEXT


@click.command(short_help = 'Initialise a directory with base files')
@click.option('-d', '--directory', default='.', help='Target a specific directory (default: cwd)')
def init(directory):
    endpoints_file = directory + '/endpoints'
    task_file = directory + '/task'

    with open(endpoints_file, 'w+') as endpoints:
        endpoints.write(ENDPOINTS_BASE_TEXT)

    if click.confirm('Edit endpoints now?'):
        utils.edit_file(endpoints_file)

    with open(task_file, 'w+') as task:
        task.write(TASK_BASE_TEXT)

    if click.confirm('Edit task now?'):
        utils.edit_file(task_file)
