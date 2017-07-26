#! /usr/bin/env python

from moss.framework.core.task import task_control

def run_cli_run_task_from_file(endpoints, output_file, print_output, task):
    '''
    Summary.
    TFW there's more comments than code. This just initiates a task.
    '''

    task_control(endpoints, output_file, print_output, task)
