#! /usr/bin/env python

import click

from moss.framework.management.new import new_cli_create_endpoints_file, new_cli_create_module_file, new_cli_create_task_file


@click.command(short_help = 'Create new endpoints template')
@click.option('-e', '--edit', is_flag=True, help = 'Edit the template now')
@click.option('-o', '--output', default='endpoints', help = 'Filename for output file')
def endpoints(edit, output):
    new_cli_create_endpoints_file(edit, output)


@click.command(short_help = 'Create new module template')
@click.option('-e', '--edit', is_flag=True, help = 'Edit the template now')
@click.option('-o', '--output', default='module', help = 'Filename for output file')
def module(edit, output):
    new_cli_create_module_file(edit, output)


@click.command(short_help = 'Create new task template')
@click.option('-e', '--edit', is_flag=True, help = 'Edit the template now')
@click.option('-o', '--output', default='task', help = 'Filename for output file')
def task(edit, output):
    new_cli_create_task_file(edit, output)


@click.group(short_help = 'Create new templates for endpoints, tasks, or custom modules')
def new():
    pass


new.add_command(endpoints)
new.add_command(module)
new.add_command(task)
