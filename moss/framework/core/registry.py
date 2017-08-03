#! /usr/bin/env python

import os
import json
import uuid
import inspect

from moss.framework.core.log import log

registered_operations = {}

def registry(group, platform, func):
    '''
    Summary:
    Store functions from devops and user created module in the registry. That way
    only devops scripts and modules decorated with @register can be ran. Modules
    must be registered before they can be ran in a task

    Arguments:
    group           string, name of group script should be stored in
    platform        string, platform devop or module is written to run on
    func            string, name of function to be ran
    '''

    if group not in registered_operations:
        registered_operations[group] = {}

    if not registered_operations[group].get(platform):
        registered_operations[group][platform] = {}
    try:
        registered_operations[group][platform].update({func.__name__: func})
    except:
        pass


def _run_registered_operation(group, platform, operation, connection, **kwargs):
    '''
    Summary:
    Wrapper to be used internally, used to the same effect as framework.core.module.execute_device_operation.

    Arguments:
    group           string, name of the group to which the script belongs
    platform        string, platform the operation is categorised by
    operation       string, operation to be run
    connection      netmiko SSH obj, connection to used to run the operaiton
    **kwargs        optional arguments the operation needs to run
    '''

    log('Attempting to run {}'.format(operation))

    result = registered_operations[group][platform][operation](connection, **kwargs)

    if isinstance(result, dict):
        module_result = result
    elif callable(result):
        module_result = result()
    else:
        module_result = {'result': 'success'}

    log('Successfully ran {}'.format(operation))
    module_result.update({'uuid': str(uuid.uuid4())})

    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe, 2)

    file_data = {}
    file_data[operation] = {}
    file_data[operation].update(module_result)

    for key, index in registered_operations['modules'][platform].iteritems():
        if calframe[2][3] in key:
            with open('output/.links.json', 'r') as temp_links_file:
                links_data = json.load(temp_links_file)

            links_data['links'].update({calframe[2][3]: operation})

            with open('output/.links.json', 'w') as temp_links_file:
                json.dump(links_data, temp_links_file, indent = 4)

    with open('output/.stdout.json', 'r') as temp_module_output:
        module_data = json.load(temp_module_output)

    module_data['module_results'].update(file_data)

    with open('output/.stdout.json', 'w') as temp_module_output:
        json.dump(module_data, temp_module_output, indent = 4)

    return result
