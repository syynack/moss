#! /usr/bin/env python

registered_operations = {'devops': {}, 'modules': {}}

def register(platform):
    '''
    Summary:
    Takes modules registered with the @register decorator. Aim is to only allow
    registered modules to be executed. The modules are appended to a list
    which is ordered by platform.

    Arguments:
    platform        string, platform module is intended to be used for

    Returns:
    func
    '''

    def decorator(func):
        if isinstance(platform, str):
            if 'moss.devops.' in str(func.__module__):
                _register('devops', platform, func)
            else:
                _register('modules', platform, func)
        return func
    return decorator


def _register(_type, platform, func):
    if not registered_operations[_type].get(platform):
        registered_operations[_type][platform] = {}
    try:
        registered_operations[_type][platform].update({func.__name__: func})
    except:
        pass
