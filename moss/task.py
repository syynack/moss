#! /usr/bin/env python

import json
import sys
import socket

from utils import start_banner, start_header, timer, runtime, end_banner
from core import update_module_order, run_module
from datetime import datetime
from getpass import getuser


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
