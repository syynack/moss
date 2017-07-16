#! /usr/bin/env python

import click
import yaml
import sys
import getpass
import socket

from moss.device import Device
from moss.task import run_task
from moss.utils import print_data_in_json, write_json_to_file


def _parse_yaml_data_to_dict(*args):
    yaml_data = []

    for target_file in args:
        try:
            with open(target_file, 'r') as yaml_file:
                try:
                    yaml_data.append(yaml.load(yaml_file))
                except yaml.YAMLError as e:
                    print e
        except IOError as e:
            error = str(e)
            print 'Cannot find file {}'.format(str(error.split('directory')[1][4:-1]))
            sys.exit(1)

    return yaml_data


def _construct_task_order(task_data):
    task_order = []

    for task in task_data:
        task_order.append({
            'module': task.get('module'),
            'argument': task.get('argument'),
            'success_outcome': 'success' if not task.get('success_outcome') else task.get('success_outcome'),
            'failure_next_module': task.get('failure_next_module'),
            'focus': task.get('focus'),
            'focus_outcome': task.get('focus_outcome'),
            'final': task.get('final')
        })

    return task_order


def _construct_endpoint(endpoint, endpoint_data):
    username_sources = [endpoint['username'], endpoint_data['global_username'], getpass.getuser()]
    password_sources = [endpoint['password'], endpoint_data['global_password']]

    username = next(username for username in username_sources if username is not '')
    password = next(password for password in password_sources if username is not '')

    device = Device(
        device_type = endpoint.get('os') if endpoint.get('os') else endpoint_data.get('global_os'),
        ip = endpoint.get('ip'),
        username = username,
        password = '' if endpoint_data.get('key_file') else password,
        port = 22 if endpoint.get('port') is None else endpoint['port'],
        timeout = 8 if endpoint.get('timeout') is None else endpoint['timeout'],
        session_timeout = 60 if endpoint.get('session_timeout') is None else endpoint['session_timeout']
    )

    return device


@click.command(short_help = 'Run a task from predefined files')
@click.option('-e', '--endpoints', default='endpoints', help='File containing endpoint information (default: endpoints)')
@click.option('-o', '--output-file', default='', help='Write the output of the task to a file')
@click.option('-p', '--print-output', is_flag=True, help='Print the JSON output of the task to the screen')
@click.option('-t', '--task', default='task', help='File containing task information (default: task)')
def run(endpoints, output_file, print_output, task):
    endpoint_data, task_data = _parse_yaml_data_to_dict(endpoints, task)
    module_order = _construct_task_order(task_data['task'])

    for endpoint in endpoint_data['endpoints']:
        endpoint_obj = _construct_endpoint(endpoint, endpoint_data)
        endpoint_connection = endpoint_obj.get_connection()
        result = run_task(endpoint_connection, module_order)

        endpoint_obj.close(endpoint_connection)

        if print_output:
            print_data_in_json(result)

        if output_file:
            write_json_to_file(result, output_file)
