#! /usr/bin/env python

import sys

from utils import *
from modules.decorators import *

def run_module(connection, module_data):
    '''
    Summary:
    I know, you're thinking "what on earth has he done here?". Me too, let me
    explain. This works by looking at the task names in module_data (just the string),
    it will then call that actual function based off the string. It will then
    have to call the subfunctions as well as they are from decorators.py
    The result data will then be returned.

    Arguments:
    connection          Netmiko SSH object
    module_data           list, from task_orchestrator

    Returns:
    dict
    '''

    module_start_time = timer()
    module_start_header(module_data['module'])

    target_mod = __import__('modules.' + connection.device_type, globals(), locals(), ['object'], -1)
    target_func = getattr(target_mod, module_data['module'])

    try:
        result = target_func(connection)
    except TypeError as e:
        print str(e)

    module_end_header(result['result'])
    module_end_time = timer()
    module_run_time = runtime(module_start_time, module_end_time)

    module_result = 'success'
    next_module = module_data['next_module']

    # Check if we got the result we wanted
    if result['result'] != module_data['success_outcome']:
        module_result = 'fail'
        if module_data['failure_next_module'] == None:
            end_banner(result['result'])
            print colour(' :: No failure_next_task specified and success_outcome is not failure for {}. Exiting.\n' \
                .format(module_data['module']), 'red'
            )

            sys.exit()

        next_module = module_data['failure_next_module']
        task_branch_header(next_module)

    print ''

    # Make some new data
    module_result_dict = {
        'module': {
            'namespace': result['namespace'],
            'name': result['task'],
            'result': module_result
        },
        'result': result['result'],
        'stdout': result['stdout'],
        'start_time': module_start_time,
        'end_time': module_end_time,
        'run_time': module_run_time,
        'next_module': next_module
    }

    return module_result_dict


def update_module_order(module_order):
    '''
    Summary:
    Goes through the current task list and adds the next task for each one

    Arguments:
    module_data           list, from task_orchestrator

    Returns:
    list
    '''

    for index, module in enumerate(module_order[:-1]):
        if not module['final']:
            module['next_module'] = module_order[index + 1]['module']
        else:
            module['next_module'] = 'end'

    module_order[-1]['next_module'] = 'end'

    return module_order
