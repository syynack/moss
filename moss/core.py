#! /usr/bin/env python

import sys

from utils import *
from framework.decorators import *

def run_task(connection, task_data):
    '''
    Summary:
    I know, you're thinking "what on earth has he done here?". Me too, let me
    explain. This works by looking at the task names in task_data (just the string),
    it will then call that actual function based off the string. It will then
    have to call the subfunctions as well as they are from decorators.py
    The result data will then be returned.

    Arguments:
    connection          Netmiko SSH object
    task_data           list, from task_orchestrator

    Returns:
    dict
    '''

    task_start_time = timer()
    task_start_header(task_data['task_name'])

    try:
        # See if we can get the function from decorators.py with the same name
        result = globals()[task_data['task_name']]()
    except KeyError as e:
        print colour('Unable to find function "{}".'.format(task_data['task_name']), 'red', bold=True)
        sys.exit()

    # Call the decorating function
    decorator = result(connection)

    # Check if we need to pass an arg, there's a nicer way to do this
    if task_data['argument']:
        result = decorator(connection, task_data['argument'])
    else:
        result = decorator(connection)

    task_end_header(result['result'])
    task_end_time = timer()
    task_run_time = runtime(task_start_time, task_end_time)

    task_result = 'success'
    next_task = task_data['next_task']

    # Check if we got the result we wanted
    if result['result'] != task_data['success_outcome']:
        task_result = 'fail'
        if task_data['failure_next_task'] == None:
            end_banner(result['result'])
            print colour(' :: No failure_next_task specified and success_outcome is not failure for {}. Exiting.\n' \
                .format(task_data['task_name']), 'red'
            )

            sys.exit()

        next_task = task_data['failure_next_task']
        task_branch_header(next_task)

    print ''

    # Make some new data
    task_result_dict = {
        'task': {
            'namespace': result['namespace'],
            'name': result['task'],
            'result': task_result
        },
        'result': result['result'],
        'stdout': result['stdout'],
        'start_time': task_start_time,
        'end_time': task_end_time,
        'run_time': task_run_time,
        'next_task': next_task
    }

    return task_result_dict


def update_task_list(task_data):
    '''
    Summary:
    Goes through the current task list and adds the next task for each one

    Arguments:
    task_data           list, from task_orchestrator

    Returns:
    list
    '''

    for index, task in enumerate(task_data[:-1]):
        if not task['final']:
            task['next_task'] = task_data[index + 1]['task_name']
        else:
            task['next_task'] = 'end'

    task_data[-1]['next_task'] = 'end'

    return task_data
