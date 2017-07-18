#! /usr/bin/env python

import click

from moss.task import parse_yaml_data_to_dict, construct_task_order, construct_endpoint, run_task

@click.command(short_help = 'Run a task from predefined files')
@click.option('-e', '--endpoints', default='endpoints', help='File containing endpoint information (default: endpoints)')
@click.option('-o', '--output-file', default='', help='Write the output of the task to a file')
@click.option('-p', '--print-output', is_flag=True, help='Print the JSON output of the task to the screen')
@click.option('-t', '--task', default='task', help='File containing task information (default: task)')
def run(endpoints, output_file, print_output, task):
    endpoint_data, task_data = parse_yaml_data_to_dict(endpoints, task)
    module_order = construct_task_order(task_data['task'])

    for endpoint in endpoint_data['endpoints']:
        endpoint_obj = construct_endpoint(endpoint, endpoint_data)
        endpoint_connection = endpoint_obj.get_connection()
        result = run_task(endpoint_connection, module_order)

        endpoint_obj.close(endpoint_connection)

        if print_output:
            print_data_in_json(result)

        if output_file:
            write_json_to_file(result, output_file)
