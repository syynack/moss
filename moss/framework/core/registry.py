#! /usr/bin/env python

import os
import json

from moss.framework.core.log import Logger

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

    destination_json_file = '.moss/module_output/' + operation + '.json.log'
    logger = Logger()
    logger.log('Attempting to run {}'.format(operation))

    result = registered_operations[group][platform][operation](connection, **kwargs)

    if isinstance(result, dict):
        module_result = result
    elif callable(result):
        module_result = result()
    else:
        module_result = {'result': 'success'}

    logger.log('Successfully ran {}'.format(operation))

    if os.path.exists('.moss'):
        if not os.path.exists('.moss/module_output'):
            os.makedirs('.moss/module_output')

        with open(destination_json_file, 'w') as temp_module_output:
            temp_module_output.write(json.dumps(module_result, indent=4, sort_keys=True))

    return result
