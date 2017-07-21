#! /usr/bin/env python

import click
import sys

from moss.utils import edit_file
from moss.text import TASK_BASE_TEXT, ENDPOINTS_BASE_TEXT


@click.command(short_help = 'Create new endpoints template')
@click.option('-e', '--edit', is_flag=True, help = 'Edit the template now')
def endpoints(edit):
    if edit:
        with open('endpoints', 'w+') as template:
            template.write(ENDPOINTS_BASE_TEXT)
            edit_file(template)
            sys.exit(0)

    with open('endpoints', 'w+') as template:
        template.write(ENDPOINTS_BASE_TEXT)


@click.command(short_help = 'Create new module template')
@click.option('-e', '--edit', is_flag=True, help = 'Edit the template now')
def module(edit):
    if edit:
        with open('module.py', 'w+') as template:
            template.write(MODULE_BASE_TEXT)
            edit_file(template)
            sys.exit(0)

    with open('module.py', 'w+') as template:
        template.write(MODULE_BASE_TEXT)


@click.command(short_help = 'Create new task template')
@click.option('-e', '--edit', is_flag=True, help = 'Edit the template now')
def task(edit):
    if edit:
        with open('task', 'w+') as template:
            template.write(TASK_BASE_TEXT)
            edit_file(template)
            sys.exit(0)

    with open('task', 'w+') as template:
        template.write(TASK_BASE_TEXT)


@click.group(short_help = 'Create new templates for endpoints, tasks, or custom modules')
def new():
    pass


new.add_command(endpoints)
new.add_command(module)
new.add_command(task)
