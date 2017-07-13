#! /usr/bin/env python

import json
import sys

from utils import *
from core import *


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
    start_time = timer()

    module_order = update_module_order(module_order)
    next_module = module_order[0]

    while next_module != 'end':
        result = run_module(connection, next_module)
        result_dict['modules'].append(result)

        if next_module['final']:
            break

        next_module_name = result['next_module']

        if next_module_name != 'end':
            module_index = [index for index, module in enumerate(module_order) if next_module_name in module['module']]
            next_module = module_order[module_index[0]]
        else:
            next_module = next_module_name

    end_time = timer()
    run_time = runtime(start_time, end_time)

    result_dict.update({
        'start_time': start_time,
        'end_time': end_time,
        'run_time': run_time
    })

    end_banner(result_dict['modules'][-1]['result'])
    return result_dict
