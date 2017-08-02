#! /usr/bin/env python

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
