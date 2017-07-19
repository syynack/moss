#! /usr/bin/env python

import click

from moss.task import task_control

@click.command(short_help = 'Run a task from predefined files')
@click.option('-e', '--endpoints', default='endpoints', help='File containing endpoint information (default: endpoints)')
@click.option('-o', '--output-file', default='', help='Write the output of the task to a file')
@click.option('-p', '--print-output', is_flag=True, help='Print the JSON output of the task to the screen')
@click.option('-t', '--task', default='task', help='File containing task information (default: task)')
def run(endpoints, output_file, print_output, task):
    task_control(endpoints, output_file, print_output, task)
