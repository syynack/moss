#! /usr/bin/env python

from moss.framework.core.task import task_control

def run_cli_run_task_from_file(endpoints, output_file, print_output, task):
    task_control(endpoints, output_file, print_output, task)
