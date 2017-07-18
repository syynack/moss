#! /usr/bin/env python

import sys
import socket
import click
import yaml
import getpass

from moss.utils import start_banner, start_header, timer, runtime, end_banner, print_data_in_json, write_json_to_file
from moss.core import update_module_order, run_module
from moss.device import Device

from datetime import datetime
from getpass import getuser


def parse_yaml_data_to_dict(*args):
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


def construct_task_order(task_data):
    task_order = []

    for task in task_data:
        task_order.append({
            'module': task.get('module'),
            'argument': task.get('argument'),
            'success_outcome': 'success' if not task.get('success_outcome') else task.get('success_outcome'),
            'failure_next_module': task.get('failure_next_module'),
            'focus': task.get('focus'),
            'focus_next_module': task.get('focus_next_module'),
            'final': False if not task.get('final') else task.get('final')
        })

    return task_order


def construct_endpoint(endpoint, endpoint_data):
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


def run_task(connection, module_order):
    '''
    Summary:
    Runs tasks that were defined through .add_task in a structured way.

    Arguments:
    connection

    Returns:
    dict
    '''

    start_banner()
    start_header(module_order)

    result_dict = {'modules': []}
    start_timer = timer()
    start_time = str(datetime.now())
    user = getuser()

    final = False
    module_order = update_module_order(module_order)
    next_module = module_order[0]

    while not final:
        result = run_module(connection, next_module)
        result_dict['modules'].append(result)

        next_module_name = result['next_module']

        if next_module_name:
            module_index = [index for index, module in enumerate(module_order) if next_module_name in module['module']]
            next_module = module_order[module_index[0]]
        else:
            if next_module['final']:
                final = True
            else:
                print ''
                end_banner(module_result)
                print colour(' :: Could not find next module or final data.\n', 'white')

    end_timer = timer()
    end_time = str(datetime.now())
    run_time = runtime(start_timer, end_timer)

    result_dict['task_info'] = {}

    result_dict['task_info'].update({
        'start_time': start_time,
        'end_time': end_time,
        'run_time': run_time,
        'user': user,
        'hostname': socket.gethostname()
    })

    end_banner(result_dict['modules'][-1]['result'])
    return result_dict
