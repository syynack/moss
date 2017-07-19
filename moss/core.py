#! /usr/bin/env python

import sys
import inspect

from moss.register import REGISTER as register
from moss.utils import runtime, timer, module_start_header, module_end_header, end_banner, module_branch_header, colour, module_focus_match_banner
from datetime import datetime

def _check_focus(focus, stdout):
    '''
    Summary:
    Iterates through stdout and uses recursion to find a match for focus. Matches
    are appended to focus_matches and returned in a list.

    Arguments:
    focus            dict, key value pair to be matched
    stdout           dict or list, result of the module

    Returns:
    list
    '''

    focus_matches = []
    focus_key = next(iter(focus))

    if isinstance(stdout, list):
        for entry in stdout:
            if isinstance(entry, dict):
                results = _check_focus(focus, entry)
                for result in results:
                    focus_matches.append(result)
    elif isinstance(stdout, dict):
        for key, value in stdout.iteritems():
            if key == focus_key:
                if stdout[key] == focus[focus_key]:
                    focus_matches.append({key: value})
            elif isinstance(value, dict):
                results = _check_focus(focus, value)
                for result in results:
                    focus_matches.append(result)
            elif isinstance(value, list):
                results = _check_focus(focus, value)
                for result in results:
                    focus_matches.append(result)
    else:
        if focus_key in stdout:
            focus_matches.append(stdout[focus])

    return focus_matches


def run_module(connection, module_data):
    '''
    Summary:
    Queries register for the module it needs to run, executes it, parses the output
    for focus or for success_outcome. Returns along with module run data.

    Arguments:
    connection          Netmiko SSH object
    module_data         list, from task_orchestrator

    Returns:
    dict
    '''

    module_start_timer = timer()
    module_start_time = str(datetime.now())
    module_start_header(module_data['module'])

    if not register.get(connection.device_type).get(module_data['module']):
        print ''
        end_banner('fail')
        print colour(' :: Could not find {}. Is it registered?\n'.format(module_data['module']), 'white')
        sys.exit(1)

    kwargs = {'connection': connection}

    try:
        kwargs.update(module_data.get('arguments'))
    except TypeError as e:
        pass

    try:
        result = register[connection.device_type][module_data['module']](**kwargs)
    except TypeError as e:
        print ''
        end_banner('fail')
        print colour(' :: {} takes {}\n'.format(module_data.get('module'), \
            ', '.join(inspect.getargspec(register[connection.device_type][module_data['module']])[0][1:])), 'white')
        sys.exit(1)

    if module_data.get('focus'):
        focus_result = _check_focus(module_data['focus'], result['stdout'])
        if focus_result:
            result['focus_outcome'] = True
            result['focus_result'] = focus_result

    module_end_header(result['result'])
    module_end_timer = timer()
    module_end_time = str(datetime.now())
    module_run_time = runtime(module_start_timer, module_end_timer)

    module_result = 'success'
    next_module = module_data.get('next_module')

    if result.get('focus_outcome'):
        result['result'] = module_data['success_outcome']

        if module_data.get('focus_next_module'):
            next_module = module_data['focus_next_module']
            module_focus_match_banner(next_module)
        else:
            module_focus_match_banner(None)

    if result['result'] != module_data['success_outcome']:
        module_result = 'fail'
        if module_data['failure_next_module'] == None:
            print ''
            end_banner(module_result)
            print colour(' :: No failure_next_task specified and success_outcome is not failure for {}.\n' \
                .format(module_data['module']), 'white'
            )
            sys.exit(1)

        next_module = module_data['failure_next_module']
        module_branch_header(next_module)

    print ''

    return {
        'module': {
            'namespace': result['namespace'],
            'name': result['task'],
            'result': module_result
        },
        'result': result['result'],
        'focus_result': result.get('focus_result'),
        'stdout': result['stdout'],
        'start_time': module_start_time,
        'end_time': module_end_time,
        'run_time': module_run_time,
        'next_module': next_module
    }


def update_module_order(module_order):
    '''
    Summary:
    Goes through the current task list and adds the next task for each one

    Arguments:
    module_data           list, from moss.task

    Returns:
    list
    '''

    for index, module in enumerate(module_order[:-1]):
        if not module['final']:
            module['next_module'] = module_order[index + 1]['module']
        else:
            module['next_module'] = ''

    module_order[-1]['final'] = True
    return module_order
