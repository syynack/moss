#! /usr/bin/env python

import sys
import socket
import click
import yaml
import getpass

<<<<<<< HEAD:moss/framework/core/task.py
from moss.framework.core.endpoint import Endpoint
from moss.framework.core.module import Module
from moss.framework.utils import start_banner, start_header, timer, end_banner, write_json_to_file
=======
from moss.endpoint import Endpoint
from moss.module import Module
from moss.utils import start_banner, start_header, timer, end_banner, write_json_to_file
>>>>>>> ab66192... Significant changes to the way modules work and the way tasks use them to run:moss/task.py
from datetime import datetime
from getpass import getuser


def _task_start_signals(module_order):
    start_banner()
    start_header(module_order)

    return {
        'results': {
            'modules': []
        },
        'start_time': timer(),
        'start_date_time': str(datetime.now()),
        'start_user': getpass.getuser(),
        'start_hostname': socket.gethostname()
    }


def _task_end_signals(start_data):
    end_banner(start_data['results']['modules'][-1]['result'])
    end_data = {
        'end_time': timer(),
        'end_date_time': str(datetime.now()),
        'run_time': timer() - start_data['start_time']
    }
    end_data.update(start_data)
    return end_data


def _parse_yaml_data(*args):
    '''
    Summary:
    Takes YAML data from endpoint and task files and returns as list of dicts

    Arguments:
    *args           filenames to be parsed

    Returns:
    list
    '''

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
    '''
    Summary:
    Constructs the correct task order for the task with default outcomes.

    Arguments:
    task_data           list, task_data['task'] returned from parse_yaml_data

    Returns:
    list
    '''

    module_order = []

    for module in task_data:
        module_order.append({'module': module})

    for index, module in enumerate(module_order[:-1]):
        module['next_module'] = module_order[index + 1]['module']

    module_order[-1]['next_module'] = ''

    return module_order


def _construct_endpoint(endpoint, endpoint_data):
    '''
    Parses dict from endpoints file to construct an endpoints obj with the correct information.

    Arguments:
    endpoint        dict, data from the endpoints file containing connection information
    endpoint_data   dict, entire endpoint data

    Return:
    moss Device object containing netmiko SSH object
    '''

    username_sources = [endpoint['username'], endpoint_data['global_username'], getpass.getuser()]
    password_sources = [endpoint['password'], endpoint_data['global_password']]

    username = next(username for username in username_sources if username is not '')
    password = next(password for password in password_sources if username is not '')

    device = Endpoint(
        device_type = endpoint.get('os') if endpoint.get('os') else endpoint_data.get('global_os'),
        ip = endpoint.get('ip'),
        username = username,
        password = '' if endpoint_data.get('key_file') else password,
        port = 22 if endpoint.get('port') is None else endpoint['port'],
        timeout = 8 if endpoint.get('timeout') is None else endpoint['timeout'],
        session_timeout = 60 if endpoint.get('session_timeout') is None else endpoint['session_timeout']
    )

    return device


def _run_task(connection, module_order):
    next_module = module_order[0]
    start_data = _task_start_signals(module_order)

    while next_module != '':
        module = Module(
            connection = connection,
            module = next_module['module'],
            next_module = next_module['next_module']
        )

        result = module.run()
        next_module = result['next_module']
        start_data['results']['modules'].append(result)

        if next_module != '':
            module_index = [index for index, module in enumerate(module_order) if next_module == module['module']]

            if not module_index:
                next_module = ''
            else:
                next_module = module_order[module_index[0]]

    end_data = _task_end_signals(start_data)
    write_json_to_file(end_data, '.moss/task-{}.json'.format(str(datetime.now())))


def task_control(endpoints, output_file, print_output, task):
    '''
    Summary:
    Controlling for the overall execution of the task, controls running each
    module for each endpoints

    Arguments:
    endpoints           file, containing endpoint information
    output_file         file, optional output file
    print_output        option, print the output in JSON
    task                file, containing task information

    Returns:
    file or JSON output
    '''

    endpoint_data, task_data = _parse_yaml_data(endpoints, task)
    module_order = _construct_task_order(task_data['task'])

    for endpoint in endpoint_data['endpoints']:
        endpoint_obj = _construct_endpoint(endpoint, endpoint_data)
        endpoint_connection = endpoint_obj.get_connection()
        result = _run_task(endpoint_connection, module_order)

        endpoint_obj.close(endpoint_connection)

        if print_output:
            print_data_in_json(result)

        if output_file:
            write_json_to_file(result, output_file)
