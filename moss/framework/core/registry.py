#! /usr/bin/env python

registered_operations = {'devops': {}, 'modules': {}}

def registry(_type, platform, func):
    '''
    Summary:
    Store functions from devops and user created module in the registry. That way
    only devops scripts and modules decorated with @register can be ran. Modules
    must be registered before they can be ran in a task

    Arguments:
    _type           string, either devops or modules
    platform        string, platform devop or module is written to run on
    func            string, name of function to be ran
    '''

    if not registered_operations[_type].get(platform):
        registered_operations[_type][platform] = {}
    try:
        registered_operations[_type][platform].update({func.__name__: func})
    except:
        pass
